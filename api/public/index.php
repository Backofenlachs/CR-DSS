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
    // error_log(print_r($applicantData, true));

    $applicantNumber = 'APP-0001';

    // ========== Loan Request ==========
    $finalApplicantData = enrichApplicantData($applicantData, $applicantNumber);


    $jsonData = json_encode($finalApplicantData, JSON_PRETTY_PRINT);    // data in jsonData formating
    
    $dataDir = '../../data/';
    $requestFileName = $applicantNumber.'_loan-request.json';

    try {
        file_put_contents($dataDir.$requestFileName, $jsonData); 
    } catch(Throwable $th) {
        throw new Exception('Writing data Failed');
    }


    // ========== Loan Result ==========
    


    // check when ../../data/APP-0001-loan-result.json is final

    // read data from loan-result and return to frontend


    $data = [
        'meta' => [
            'success' => true,
            'timestamp' => date(DATE_ATOM)
        ],
        'data' => [
            'applicant_number' => $applicantNumber,
            'result' => 'APPROVED'
        ]
    ];

    $response->getBody()->write(json_encode($data));

    return $response
        ->withHeader('Content-Type', 'application/json')
        ->withHeader('Access-Control-Allow-Origin', '*');
});

$app->options('/{routes:.*}', function (Request $request, Response $response): Response {
    return $response
        ->withHeader('Access-Control-Allow-Origin', '*')
        ->withHeader('Access-Control-Allow-Headers', 'Content-Type')
        ->withHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
});

$app->run();


// TEMP: enrichment + data validation
function enrichApplicantData(array $data, string $applicantNumber): array {

    $data['application_number'] = $applicantNumber;
    
    return $data;
}   