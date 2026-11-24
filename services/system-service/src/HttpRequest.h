#pragma once

#ifndef HTTPREQUEST_H
#define HTTPREQUEST_H

#include<string>
#include<unordered_map>



struct HttpRequest {
    
    std::string method;
    std::string target;
    std::string version;
    
    std::unordered_map<std::string, std::string> headers;

    enum class ParseStatus {
        Success,
        BadRequest,
        Incomplete
    };

    static ParseStatus parse(const std::string& request_string, HttpRequest& request);
};

#endif
