from sms_ir import SmsIr


def send_forget_password_sms(number_phone, token):
    message = f'https://codena.org/accounts/change-password/{token}/ '
    sms_ir = SmsIr(
        api_key='d1MLHDnIHueFhji3NpGAcwkslZeloafMGqD3sgw4dVmqQTVZOctoGb3KMj4e9QIK',
        linenumber='30007732010355',
    )
    print(token)

    sms_ir.send_verify_code(
        number=str(number_phone),
        template_id=273118,
        parameters=[
            {
                "name": "CODE",
                "value": token,
            },
        ],
    )