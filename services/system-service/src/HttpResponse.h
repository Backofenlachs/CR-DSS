#pragma once

#ifndef HTTPRESPONSE_H
#define HTTPRESPONSE_H

#include<string>

struct HttpResponse {

    std::string version = "HTTP/1.1";
    int status;
    std::string content_type = "application/json";
    std::string body;

    // erstmal noch keine status zurückgeben. weil es ein internes objekt ist. das sollte im optimalfall richtig sein.
    std::string serialize() const; // darf die member lesen, aber nicht verändern
};

#endif