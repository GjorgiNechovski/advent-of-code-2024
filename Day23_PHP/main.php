<?php

function readConnections($filePath) {
    $connections = [];
    $file = fopen($filePath, 'r');
    while (($line = fgets($file)) !== false) {
        [$a, $b] = explode('-', trim($line));
        if (!isset($connections[$a])) $connections[$a] = [];
        if (!isset($connections[$b])) $connections[$b] = [];
        $connections[$a][] = $b;
        $connections[$b][] = $a;
    }
    fclose($file);

    foreach ($connections as $key => $value) {
        $connections[$key] = array_unique($value);
    }

    return $connections;
}

function countTripletsWithT($connections) {
    $keys = array_keys($connections);
    sort($keys);
    $count = 0;

    for ($i = 0; $i < count($keys); $i++) {
        for ($j = $i + 1; $j < count($keys); $j++) {
            for ($k = $j + 1; $k < count($keys); $k++) {
                $a = $keys[$i];
                $b = $keys[$j];
                $c = $keys[$k];

                if (in_array($b, $connections[$a]) && in_array($c, $connections[$a]) && in_array($c, $connections[$b])) {
                    if (str_starts_with($a, 't') || str_starts_with($b, 't') || str_starts_with($c, 't')) {
                        $count++;
                    }
                }
            }
        }
    }

    return $count;
}

function findLargestSet($connections) {
    $keys = array_keys($connections);
    $best = [];

    for ($t = 0; $t < 1000; $t++) {
        shuffle($keys);
        $set = [];

        foreach ($keys as $node) {
            $ok = true;
            foreach ($set as $y) {
                if (!in_array($node, $connections[$y])) {
                    $ok = false;
                    break;
                }
            }

            if ($ok) {
                $set[] = $node;
            }
        }

        if (count($set) > count($best)) {
            $best = $set;
        }
    }

    sort($best);
    return $best;
}

$filePath = '1.txt';
$connections = readConnections($filePath);

$p1 = countTripletsWithT($connections);

$largestClique = findLargestSet($connections);

echo "$p1\n";
echo implode(',', $largestClique);

?>