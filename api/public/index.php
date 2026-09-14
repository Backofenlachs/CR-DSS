<?php

use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

require __DIR__ . '/../vendor/autoload.php';

$app = AppFactory::create();

$app->get('/', function (Request $request, Response $response): Response {
    $response->getBody()->write('Hello World');

    return $response;
});

$app->post('/api/risk-assessment', function (Request $request, Response $response): Response {
    $body = json_decode((string) $request->getBody(), true);

    $applicantData = $body['data'];

    error_log(print_r($applicantData, true));

    $data = [
        'meta' => [
            'success' => true,
            'timestamp' => date(DATE_ATOM)
        ],
        'data' => [
            'applicant_number' => 'APP-0001',
            'result' => 'APPROVED'
        ]
    ];

    $response->getBody()->write(json_encode($data));

    return $response
        ->withHeader('Content-Type', 'application/json')
        ->withHeader('Access-Control-Allow-Origin', '*');
});


$app->options('/{routes:.*}', function (
    Request $request,
    Response $response
): Response {
    return $response
        ->withHeader('Access-Control-Allow-Origin', '*')
        ->withHeader('Access-Control-Allow-Headers', 'Content-Type')
        ->withHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
});

$app->run();