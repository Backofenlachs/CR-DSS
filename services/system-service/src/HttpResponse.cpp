#include "HttpResponse.h"

std::string HttpResponse::serialize() const {
    
    // TODO: Validate HTTP response fields before serialization.
    // TODO: Resolve status reason phrase based on HTTP status code.

    std::string res = version + " " + std::to_string(status) + " OK\r\n";
    res += "Content-Type: " + content_type + "\r\n";
    res += "Content-Length: " + std::to_string(body.size()) + "\r\n";
    res += "Connection: close\r\n";
    res += "\r\n";
    res += body;

    return res;
}