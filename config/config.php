<?php

// ---------------- Database configuration ----------------
define('DB_HOST', 'localhost');
define('DB_NAME', 'ticket_support_db');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_CHARSET', 'utf8mb4');

// ---------------- App configuration ----------------
define('APP_NAME', 'Ticket Support System');
define('APP_URL', 'http://localhost/ticket-support/public');
define('BASE_PATH', dirname(__DIR__));

// ---------------- Session ----------------
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// ---------------- Error reporting ----------------
// ปิด display_errors ตอนขึ้น production จริง
error_reporting(E_ALL);
ini_set('display_errors', 1);
