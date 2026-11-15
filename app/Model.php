<?php

require_once __DIR__ . '/Database.php';

/**
 * Model - base class ให้ Model ตัวอื่นสืบทอด (เช่น Ticket, User)
 * มี CRUD พื้นฐานครบ ตัวลูกแค่กำหนด $table แล้วเพิ่ม method เฉพาะของตัวเอง
 */
abstract class Model
{
    protected PDO $db;
    protected string $table;
    protected string $primaryKey = 'id';

    public function __construct()
    {
        $this->db = Database::getInstance()->getConnection();
    }

    public function all(string $orderBy = 'id DESC'): array
    {
        $sql = "SELECT * FROM {$this->table} ORDER BY {$orderBy}";
        $stmt = $this->db->query($sql);
        return $stmt->fetchAll();
    }

    public function find(int $id): array|false
    {
        $sql = "SELECT * FROM {$this->table} WHERE {$this->primaryKey} = :id LIMIT 1";
        $stmt = $this->db->prepare($sql);
        $stmt->execute(['id' => $id]);
        return $stmt->fetch();
    }

    public function where(string $column, mixed $value, string $operator = '='): array
    {
        $sql = "SELECT * FROM {$this->table} WHERE {$column} {$operator} :value";
        $stmt = $this->db->prepare($sql);
        $stmt->execute(['value' => $value]);
        return $stmt->fetchAll();
    }

    public function create(array $data): int
    {
        $columns = implode(', ', array_keys($data));
        $placeholders = ':' . implode(', :', array_keys($data));

        $sql = "INSERT INTO {$this->table} ({$columns}) VALUES ({$placeholders})";
        $stmt = $this->db->prepare($sql);
        $stmt->execute($data);

        return (int) $this->db->lastInsertId();
    }

    public function update(int $id, array $data): bool
    {
        $set = [];
        foreach (array_keys($data) as $column) {
            $set[] = "{$column} = :{$column}";
        }
        $setClause = implode(', ', $set);

        $sql = "UPDATE {$this->table} SET {$setClause} WHERE {$this->primaryKey} = :id";
        $data['id'] = $id;

        $stmt = $this->db->prepare($sql);
        return $stmt->execute($data);
    }

    public function delete(int $id): bool
    {
        $sql = "DELETE FROM {$this->table} WHERE {$this->primaryKey} = :id";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute(['id' => $id]);
    }

    public function count(): int
    {
        $sql = "SELECT COUNT(*) as total FROM {$this->table}";
        $stmt = $this->db->query($sql);
        return (int) $stmt->fetch()['total'];
    }
}
