import pywebio


# 数字输入
# age = pywebio.input.input("How old are you?",type=pywebio.input.NUMBER)
# pywebio.output.put_text("your age is %d"%age)

# 密码输入
password = pywebio.input.input("Input password", type=pywebio.input.PASSWORD)
# 密码获取的仍然是字符串
# 类型转换
password = int(password)
pywebio.output.put_text("your password is %d"%password)

# # Drop-down selection
# gift = select('Which gift you want?', ['keyboard', 'ipad'])

# # Checkbox
# agree = checkbox("User Term", options=['I agree to terms and conditions'])

# # Single choice
# answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

# # Multi-line text input
# text = textarea('Text Area', rows=3, placeholder='Some text')

# # File Upload
# img = file_upload("Select a image:", accept="image/*")
