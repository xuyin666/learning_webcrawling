# set cookies

import requests

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + "" + value)

# headers = {
#     'Cookie': '_device_id=a676aed7475e672130f52548eb743e14; \
#         _octo=GH1.1.821664863.1640422760; preferred_color_mode=light; \
#             tz=Asia%2FShanghai; user_session=23Qi9cxaEMEzfZCcFuM91oqEqNiXvv9H9CJEgAHEx8yrY6xf; \
#                 __Host-user_session_same_site=23Qi9cxaEMEzfZCcFuM91oqEqNiXvv9H9CJEgAHEx8yrY6xf; \
#                     tz=Asia%2FShanghai; \
#                     color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; \
#                         logged_in=yes; dotcom_user=xuyin666; has_recent_activity=1; _gh_sess=rt2yrwvgoCiE6jb57wJdk%2BUOanueLA95EueUrr2IYsJnPAQ%2BAEv5BvztQcX9Voxk%2FkyTngCHiCZeJpCVm0dVbbN8ynyUAewQtg7%2Fj3dtWQEQDGcPCx%2BA%2Bi4oNVFk9Go1c%2BjvoE8c1%2FjznEUeuS2PX0Z2ubMxGNCt47QKwmxs9krFZJIYhXb97wBqpw1hiPbEy9M1UptCwgcj6DVLnjFmSsdIMJfTSafkgvtsmR64HR2Ow9%2Fi7HOkaHNhgJ6DyGy3B6RGwVFEv2%2F1Ulq5GYqLZatWrhrfaB42PFZ%2By7e4mUqxinlHWzLNfF08Gnf%2FsuD%2F0ClWTmNrhNSZ1p2sf8Cjh3cg9Ci9T8JWPBLarMYqXupXhINtPjbr7Td4v%2FA2zmuHSHCqOYsw69K%2FAnoLVMM9%2FQd%2BFxRdT53wE%2Bk%2BmClGljSiCown7EHp0YiDazSFAo08q%2FAiRurQC3fN8uH%2Flp1rzqASCnQijgMh%2B%2BhBK05yfjB96apq8QeWIwaxJjFmfaQBDuRTv8Nj8bkzTy2XVzX4avWLK8EDi1QG0cIzKQJ%2BrKiyah4jIsMq76qdFo3pYgOerjd11YecTAvv3Lfwtp8kT%2Fc%2B%2F1jOaZNkBUZ5CbYZppb2HHWPBm7b9s%2F1MibKTNdRZpE6QpYeQ%2B%2F3c8IrqSrrBD7jaeeCBJ3P86Q1pT37d9%2FL%2Bjo2w4brN%2BFm8RXRAsKtIB%2FHMqp1bvo0ZZAFpWewQNI8SKLA93mFAL8Skh8LlHT57XJqeXCHWbpQI98QlskEdEPWR5WJBCoE6Iw8PZ2KVOGL4PhTQndiNSEldaxcBHVS3GCgLduqQapAiFjleqiklGAtJp3fDlgZCsQzh%2FUrBD%2Ffaa2TAZBCjenuqDEu3BTnv6etP%2BiZ5COm10yredLG46l3LwkVFPqQTrQ%2BrgIMzyQxmynhB39AGP85jBefg4FpxqeqsNYzkYjv2rw4iMmRsu5s1XToMdCFaSHzEecb64ryduJ2fT9gNm3KBU22kzG1mf1uXuAuG%2Bh5fzbhkB4zlgf8I0If%2BPw2eyafrvaZkL8Kqv9kEnQC1aH%2BjQQbf8kMEvtESEnVC%2FchweYby1KaTyqPLkxNT0v5O4gf6%2B3sdgK7LpnCHMPk28k7l9N3Tw5bVUIWCUW8VdB%2FbRLKL0GDAmDlqD9w9o5KUKaKM1zrt0JR6aCbiU9iYNQYH36v08JB0S3705GD5jUCyv7n5ZWBdDDoI3P26%2FnXuwQ94DRd%2Fnv%2FvjD5Wsn1eexYg7T34jM0xzao--hI0kylQ%2BWzgLcnCx--DTuW67l8NJK3EtuMrp9odg%3D%3D'
# }

# r = requests.get('https://github.com', headers=headers)
# print(r.text)

cookies = '_device_id=a676aed7475e672130f52548eb743e14; \
        _octo=GH1.1.821664863.1640422760; preferred_color_mode=light; \
        tz=Asia%2FShanghai; user_session=23Qi9cxaEMEzfZCcFuM91oqEqNiXvv9H9CJEgAHEx8yrY6xf; \
        __Host-user_session_same_site=23Qi9cxaEMEzfZCcFuM91oqEqNiXvv9H9CJEgAHEx8yrY6xf; \
        tz=Asia%2FShanghai; \
        color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; \
        logged_in=yes; dotcom_user=xuyin666; has_recent_activity=1; _gh_sess=rt2yrwvgoCiE6jb57wJdk%2BUOanueLA95EueUrr2IYsJnPAQ%2BAEv5BvztQcX9Voxk%2FkyTngCHiCZeJpCVm0dVbbN8ynyUAewQtg7%2Fj3dtWQEQDGcPCx%2BA%2Bi4oNVFk9Go1c%2BjvoE8c1%2FjznEUeuS2PX0Z2ubMxGNCt47QKwmxs9krFZJIYhXb97wBqpw1hiPbEy9M1UptCwgcj6DVLnjFmSsdIMJfTSafkgvtsmR64HR2Ow9%2Fi7HOkaHNhgJ6DyGy3B6RGwVFEv2%2F1Ulq5GYqLZatWrhrfaB42PFZ%2By7e4mUqxinlHWzLNfF08Gnf%2FsuD%2F0ClWTmNrhNSZ1p2sf8Cjh3cg9Ci9T8JWPBLarMYqXupXhINtPjbr7Td4v%2FA2zmuHSHCqOYsw69K%2FAnoLVMM9%2FQd%2BFxRdT53wE%2Bk%2BmClGljSiCown7EHp0YiDazSFAo08q%2FAiRurQC3fN8uH%2Flp1rzqASCnQijgMh%2B%2BhBK05yfjB96apq8QeWIwaxJjFmfaQBDuRTv8Nj8bkzTy2XVzX4avWLK8EDi1QG0cIzKQJ%2BrKiyah4jIsMq76qdFo3pYgOerjd11YecTAvv3Lfwtp8kT%2Fc%2B%2F1jOaZNkBUZ5CbYZppb2HHWPBm7b9s%2F1MibKTNdRZpE6QpYeQ%2B%2F3c8IrqSrrBD7jaeeCBJ3P86Q1pT37d9%2FL%2Bjo2w4brN%2BFm8RXRAsKtIB%2FHMqp1bvo0ZZAFpWewQNI8SKLA93mFAL8Skh8LlHT57XJqeXCHWbpQI98QlskEdEPWR5WJBCoE6Iw8PZ2KVOGL4PhTQndiNSEldaxcBHVS3GCgLduqQapAiFjleqiklGAtJp3fDlgZCsQzh%2FUrBD%2Ffaa2TAZBCjenuqDEu3BTnv6etP%2BiZ5COm10yredLG46l3LwkVFPqQTrQ%2BrgIMzyQxmynhB39AGP85jBefg4FpxqeqsNYzkYjv2rw4iMmRsu5s1XToMdCFaSHzEecb64ryduJ2fT9gNm3KBU22kzG1mf1uXuAuG%2Bh5fzbhkB4zlgf8I0If%2BPw2eyafrvaZkL8Kqv9kEnQC1aH%2BjQQbf8kMEvtESEnVC%2FchweYby1KaTyqPLkxNT0v5O4gf6%2B3sdgK7LpnCHMPk28k7l9N3Tw5bVUIWCUW8VdB%2FbRLKL0GDAmDlqD9w9o5KUKaKM1zrt0JR6aCbiU9iYNQYH36v08JB0S3705GD5jUCyv7n5ZWBdDDoI3P26%2FnXuwQ94DRd%2Fnv%2FvjD5Wsn1eexYg7T34jM0xzao--hI0kylQ%2BWzgLcnCx--DTuW67l8NJK3EtuMrp9odg%3D%3D'

jar = requests.cookies.RequestsCookieJar()

headers = {
    'User-Agent' : 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
}

for cookie in cookies.split(';'):
    # split only once by the delimiter '='
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('https://github.com', cookies=jar, headers=headers)
print(r.text)