#include "HttpRequest.h"

#include<iostream>
#include<sstream>
#include<vector>


HttpRequest::ParseStatus HttpRequest::parse(const std::string& request_string, HttpRequest& request) {
    HttpRequest parsed_request;
    std::unordered_map<std::string, std::string> parsed_headers;

    size_t start = 0;
    size_t end = request_string.find("\r\n");

    // Check whether http headers are complete
    if (request_string.find("\r\n\r\n") == std::string::npos) {
        return ParseStatus::Incomplete;
    }

    size_t i = 0;
    size_t request_line_parts = 0;
    
    while (end != std::string::npos) { // Request Loop


        // Sobald eine leere Zeile ("\r\n\r\n") erreicht ist, endet der Header-Bereich
        if (start == end) {
            break;
        }

        std::string line = request_string.substr(start, end - start);

        size_t line_start = 0;
        size_t j = 0;
        std::string key = "";

        while (true) {              // Line Loop
            size_t space_pos = line.find(' ', line_start);
            
            std::string word = line.substr(line_start, 
                space_pos == std::string::npos 
                    ? std::string::npos 
                    : space_pos - line_start
            );

            // First line: METHOD TARGET VERSION  
            if (i == 0) {
                if (j == 0) {
                    parsed_request.method = word;
                } else if (j == 1) {
                    parsed_request.target = word;
                } else if (j == 2) {
                    parsed_request.version = word;
                }

                request_line_parts++;
            } else { // Remaining lines: HTTP headers
                if (j == 0) {
                    key = word;

                    // Remove trailing colon
                    if (!key.empty() && key.back() == ':') {
                        key.pop_back();
                    }

                    parsed_headers[key] = "";
                } else {
                    if (!parsed_headers[key].empty()) {
                        parsed_headers[key] += " ";
                    }

                    parsed_headers[key] += word;
                }
            }

            if (space_pos == std::string::npos) {
            break;
            }

            line_start = space_pos + 1;
            j++;
        }


        i++;
        start = end + 2;
        end = request_string.find("\r\n", start);
    }

    parsed_request.headers = move(parsed_headers);
   

    // Validate request line
    if (request_line_parts != 3 || 
        parsed_request.method.empty() ||
        parsed_request.target.empty() || 
        parsed_request.version.empty()) {
        
        return ParseStatus::BadRequest;
    }

    request = std::move(parsed_request);

    return ParseStatus::Success;
}