import datetime
import pyotp


if __name__ == '__main__':
    # secret key for unique otp
    secret = pyotp.random_base32()
    # time based otp
    totp = pyotp.TOTP(secret)
    # remaining interval for otp
    time_remaining = totp.interval - datetime.datetime.now().timestamp()
    print(time_remaining)
    # otp
    print(totp.now())
    # secret key
    print(secret)
    # otp verification
    print(totp.verify(totp.now()))
    # email provisioning
    print(pyotp.totp.TOTP(secret).provisioning_uri("jrbhatt18p10@gmail.com", issuer_name="Google"))
