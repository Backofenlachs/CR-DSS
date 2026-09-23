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

    $applicantId = createAPLID();
    $dataDir = '../../data/';

    // ========== Loan Request ==========
    $requestFileName = $applicantId.'_loan-request.json';

    $finalApplicantData = enrichApplicantData($applicantData, $applicantId);
    $jsonData = json_encode($finalApplicantData, JSON_PRETTY_PRINT);    // data in jsonData formating
    

    try {
        file_put_contents($dataDir.$requestFileName, $jsonData); 
    } catch(Throwable $th) {
        throw new Exception('Writing data Failed');
    }

    exec('python3 ../../src/main.py '.escapeshellarg($applicantId), $output_array, $exicCode);
    // ========== Loan Result ==========
    $resultFileName = $applicantId.'_loan-result.json';
    
    try {
        $jsonResultData = file_get_contents($dataDir.$resultFileName);
    } catch(Throwable $th) {
        throw new Exception('Reading result Data Failed');
    }
    $resultContent = json_decode($jsonResultData);


    $data = [
        'meta' => [
            'success' => true,
            'timestamp' => date(DATE_ATOM)
        ],
        'data' => $resultContent
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
function enrichApplicantData(array $data, string $applicantId): array {

    $data['application_number'] = $applicantId;
    
    return $data;
}   


// TEMP: UUIDv4 for applicant id to await raceConditions
function createAPLID() {
    $uuidv4 = sprintf( '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
        random_int(0, 0xffff),
        random_int(0, 0xffff),
        random_int(0, 0xffff),
        random_int(0, 0x0fff) | 0x4000,
        random_int(0, 0x3fff) | 0x8000,
        random_int(0, 0xffff),
        random_int(0, 0xffff),
        random_int(0, 0xffff)
    );

    return 'APP-'.$uuidv4;
}