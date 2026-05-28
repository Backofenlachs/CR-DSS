import json

class IOHandler:

    def __init__(self):
        print("created IO-Handler")
        pass
    
    def json_IO_read(self, file) -> dict:
        with open(file, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)

        return data_dict


    def json_IO_write(self, file, data):
        with open(file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def validate_required_inputs(self, REQUIRED_INPUTS, APPLICANT_DATA):
        missing_inputs = []

        for required_input in REQUIRED_INPUTS:
            if required_input not in APPLICANT_DATA:
                missing_inputs.append(required_input)

        if missing_inputs:
           raise Exception(f"missing inputs: {missing_inputs}")