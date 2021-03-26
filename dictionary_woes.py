# Function defination
def fixup_case(response):
    """
    Function for standardizing the dictionary key.
    """
    standardized_response = []
    for each in response:
        standardized_response.append({k.lower(): v for k, v in each.items() if isinstance(k, str)})
    return standardized_response

# Dummy test response
test_api_response = [{"CustomEr_name": "Wajahat","CustoMer_ID": 353},
               {"Customer_Name": "Ali","CUSTOMER_ID": 326},
                {"Customer_NaMe": "Hassan","CustoMER_id": 352},]

# Function call
test_standardized_response = fixup_case(test_api_response)
print(test_standardized_response)