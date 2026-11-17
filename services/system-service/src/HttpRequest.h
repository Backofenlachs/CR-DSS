#pragma once

#ifndef HTTPREQUEST_H
#define HTTPREQUEST_H

#include<string>

struct HttpRequest
{
    std::string method;
    std::string target;
    std::string version;
    
    static HttpRequest parse(const std::string& request_string);
};

#endif
