#include "HttpRequest.h"

#include<iostream>
#include<sstream>
#include<vector>

HttpRequest HttpRequest::parse(const std::string& request) {
    HttpRequest req{};
    std::vector<std::string> lines;

    std::cout << "=== RAW REQUEST START (" << request.size() << " Bytes) ===\n";

    size_t start = 0;
    size_t end = request.find("\r\n");

    while (end != std::string::npos) {

        // Sobald eine leere Zeile ("\r\n\r\n") erreicht ist, endet der Header-Bereich
        if (start == end) {
            break;
        }

        lines.push_back(request.substr(start, end - start));
        
        start = end + 2;
        end = request.find("\r\n", start);
    }


    for (size_t i = 0; i < lines.size(); i++) {
        std::cout << "vector[" << i << "] : " << lines[i] << std::endl;
    }
    
    //TMP: split first line for first working HttpRequest

    // TMP: split first line for first working HttpRequest
    if (!lines.empty()) std::istringstream(lines[0]) >> req.method >> req.target >> req.version;


    std::cout << "\n=== RAW REQUEST END===" << std::endl;
    return req;
}