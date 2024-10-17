from zhipuai import ZhipuAI


def connect_GLM():
    # 这里加一个读取密钥的逻辑
    APIKEY = ""


    # 打开文件并读取
    with open('../../BV_draft.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 读取文件的所有行并存储在列表中

    print(lines[0])

    # # 访问每一行,
    # for i, line in enumerate(lines):
    #     print(f"第 {i+1} 行内容: {line.strip()}")  # .strip() 去除每行末尾的换行符


    prompt = ("请扮演一名语言学家。 您的任务是根据一篇从视频中提取的文字稿进行重写润色。"
              "首先，对文字稿进行切分并添加相应的标点符号。"
              "重写过程中，需要提取原稿的主题，并保持原稿的核心内容和信息一致。"
              "同时，确保在句式、词汇和表达方式上尽量避免与原稿雷同。目标是保留原稿的整体思想和内容，通过不同的语言表达出来，使其更加新颖和独特。"
              "输出时仅保留重写后的内容。"
              "以下为原稿：")

    # 同步调用
    client = ZhipuAI(api_key=APIKEY) # 填写APIKey
    response = client.chat.completions.create(
        model="glm-4-0520",  # 填写需要调用的模型编码
        messages=[
            {"role": "user", "content": "{}".format(prompt)},
            {"role": "user", "content": "{}".format(lines[0])},
            # {"role": "user", "content": "{}".format(my_message_2)}
        ],
    )
    print(response.choices[0].message)
    return None





if __name__ == '__main__':
    print("OK")