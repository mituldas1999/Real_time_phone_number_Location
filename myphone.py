# import phonenumbers
# from phonenumbers import timezone, carrier,geocoder

# # def get_phone_details():
# #     try:
# #         # Prompt user to enter their phone number
# #         number = input("Enter your phone number (with country code, e.g., +1234567890): ")

        
# #         # Parse the phone number
# #         phone = phonenumbers.parse(number)
        
# #         # Validate the phone number
# #         if not phonenumbers.is_valid_number(phone):
# #             print("The phone number entered is not valid. Please try again.")
# #             return
        
# #         # Fetch details
# #         time_zones = timezone.time_zones_for_number(phone)
# #         sim_carrier = carrier.name_for_number(phone, "en")
# #         region = geocoder.description_for_number(phone, "en")
        
# #         # Provide default values if any detail is missing
# #         sim_carrier = sim_carrier if sim_carrier else "SIM carrier information unavailable"
# #         region = region if region else "Region information unavailable"
        
# #         # Display the phone details
# #         print("\nDetails for the entered phone number:")
# #         print(f"Phone Number: {number}")
# #         print(f"Phone Details: {phone}")
# #         print(f"Time Zone(s): {', '.join(time_zones)}")
# #         print(f"SIM Carrier: {sim_carrier}")
# #         print(f"Region: {region}")
    
# #     except phonenumbers.phonenumberutil.NumberParseException as e:
# #         print(f"Error: {e}. Ensure you enter the phone number in the correct format (e.g., +1234567890).")
# #     except EOFError:
# #         print("Input error: No input detected. Please check your terminal setup.")

# # # Run the function
# # if __name__ == "__main__":
# #     get_phone_details()


# number = input("Enter your phone number (with country code, e.g., +1234567890): ")

        
#  Parse the phone number
# phone = phonenumbers.parse(number)


number="+8801949338805"