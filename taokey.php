<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

header('Content-Type: application/json');

$admin = 'Zwrizal';
$discord = 'https://zalo.me/g/pbgoux197';
$facebook = 'https://www.facebook.com/profile.php?id=61561150671947';

session_start();

// Lấy IP làm user_id
$user_id = $_SERVER['REMOTE_ADDR'];
$firstTwoDigits = substr($user_id, 0, 2);
$tru12 = preg_replace("/[^0-9]/", "", substr($user_id, 12));
$tru5 = preg_replace("/[^0-9]/", "", substr($user_id, 5));
$tru9 = preg_replace("/[^0-9]/", "", substr($user_id, 9));
$user_id_so = preg_replace("/[^0-9]/", "", $user_id);
$tru3 = preg_replace("/[^0-9]/", "", substr($user_id_so, 3));

$currentDate = date('d');
$currentMonth = date('m');
$currentDate_sosau = intval(substr($currentDate, 1));
if ($currentDate_sosau <= 0) {
    $currentDate_sosau = 1;
}

$result = $firstTwoDigits * $currentDate + $tru3 * $currentMonth;

// Nếu bạn muốn thêm chuỗi nào đó giữa key thì gán ở đây
$remainingChars = ''; // có thể thay bằng 'XYZ' nếu cần
$keygoc = $result . $remainingChars . $tru12 . $currentDate . $tru5 . $tru9;
$tru_ngay = substr($keygoc, $currentDate_sosau);
$keygoc2 = md5($tru_ngay);
$keygoc1 = substr($keygoc2, 5, 8);
$key = 'Z-Matrix_' . $keygoc1;

// URL cần rút gọn
$url = 'https://ntp08.x10.mx/key/?key=' . $key;

// Gửi tới dịch vụ web1s
$token_web1s = '0a5f7dfa79b43de3190dc1f8cb062f9362929d05e69a0e0f1aee32dc4489fdf6';
$url_web1s = "https://yeumoney.com/QL_api.php?token=$token_web1s&url=$url&format=json";

$ch = curl_init($url_web1s);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$web1s = curl_exec($ch);

if (curl_errno($ch)) {
    echo json_encode([
        'admin' => ['author' => $admin],
        'data' => [
            'status' => 'failure',
            'message' => 'Lỗi cURL: ' . curl_error($ch),
            'url' => null
        ]
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    curl_close($ch);
    exit();
}

curl_close($ch);

$json_web1s = json_decode($web1s, true);

if (!$json_web1s || !isset($json_web1s['status'])) {
    echo json_encode([
        'admin' => ['author' => $admin],
        'data' => [
            'status' => 'failure',
            'message' => 'Phản hồi từ API không hợp lệ.',
            'url' => null
        ]
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    exit();
}

if ($json_web1s['status'] == 'error') {
    $message = 'THẤT BẠI';
    $status = 'failure';
    $link_key = null;
} else {
    $message = 'TẠO KEY THÀNH CÔNG';
    $status = 'success';
    $link_key = $json_web1s['shortenedUrl'];
}

echo json_encode([
    'admin' => ['author' => $admin],
    'data' => [
        'status' => $status,
        'message' => $message,
        'url' => $key
    ]
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
