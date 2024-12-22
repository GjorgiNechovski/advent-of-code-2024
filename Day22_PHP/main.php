<?php

function calculate($values, $mode) {
    $sum = 0;

    if ($mode === 1) {
        foreach ($values as $row) {
            $x = (int)$row;
            for ($i = 0; $i < 2000; $i++) {
                $x = (($x * 64) ^ $x) % 16777216;
                $x = (intdiv($x, 32) ^ $x) % 16777216;
                $x = (($x * 2048) ^ $x) % 16777216;
            }
            $sum += $x;
        }
    } else {
        $total = [];

        foreach ($values as $row) {
            $x = (int)$row;
            $last = $x % 10;
            $pattern = [];

            for ($i = 0; $i < 2000; $i++) {
                $x = (($x * 64) ^ $x) % 16777216;
                $x = (intdiv($x, 32) ^ $x) % 16777216;
                $x = (($x * 2048) ^ $x) % 16777216;
                $temp = $x % 10;
                $pattern[] = [$temp - $last, $temp];
                $last = $temp;
            }

            $visited = [];

            for ($i = 0; $i < count($pattern) - 4; $i++) {
                $pat = array_map(fn($p) => $p[0], array_slice($pattern, $i, 4));
                $val = $pattern[$i + 3][1];
                $sequenceKey = implode(",", $pat);

                if (!isset($visited[$sequenceKey])) {
                    $visited[$sequenceKey] = true;

                    if (!isset($total[$sequenceKey])) {
                        $total[$sequenceKey] = $val;
                    } else {
                        $total[$sequenceKey] += $val;
                    }
                }
            }
        }

        $sum = max($total);
    }

    return $sum;
}

function run($values) {
    echo calculate($values, 1) . "\n";
    echo calculate($values, 2) . "\n";
}

$filename = "1.txt";
$values = array_map('trim', file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES));
run($values);
