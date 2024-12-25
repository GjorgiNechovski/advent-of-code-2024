<?php

$file = '1.txt';
$data = trim(file_get_contents($file));

$shapes = explode("\n\n", $data);
$keys = [];
$locks = [];

foreach ($shapes as $shape) {
    $grid = explode("\n", $shape);
    $numRows = count($grid);
    $numCols = strlen($grid[0]);

    $isKey = true;
    for ($c = 0; $c < $numCols; $c++) {
        if ($grid[0][$c] === '#') {
            $isKey = false;
            break;
        }
    }

    if ($isKey) {
        $keys[] = $grid;
    } else {
        $locks[] = $grid;
    }
}

function fits($key, $lock) {
    $numRows = count($key);
    $numCols = strlen($key[0]);

    for ($r = 0; $r < $numRows; $r++) {
        for ($c = 0; $c < $numCols; $c++) {
            if ($key[$r][$c] === '#' && $lock[$r][$c] === '#') {
                return false;
            }
        }
    }

    return true;
}

$result = 0;
foreach ($keys as $key) {
    foreach ($locks as $lock) {
        if (fits($key, $lock)) {
            $result++;
        }
    }
}

echo $result;
