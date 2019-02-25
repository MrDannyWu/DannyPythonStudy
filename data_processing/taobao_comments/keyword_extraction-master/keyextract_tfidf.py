#!/usr/bin/python
# coding=utf-8
# 采用TF-IDF方法提取文本关键词
# http://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
import sys, codecs
import pandas as pd
import numpy as np
import jieba.posseg
import jieba.analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
"""
       TF-IDF权重：
           1、CountVectorizer 构建词频矩阵
           2、TfidfTransformer 构建tfidf权值计算
           3、文本的关键字
           4、对应的tfidf矩阵
"""


# 数据预处理操作：分词，去停用词，词性筛选
def dataPrepos(text, stopkey):
    l = []
    pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    seg = jieba.posseg.cut(text)  # 分词
    for i in seg:
        if i.word not in stopkey and i.flag in pos:  # 去停用词 + 词性筛选
            l.append(i.word)
    return l


# tf-idf获取文本top10关键词
def getKeywords_tfidf(data, stopkey, topK):
    # idList, titleList, abstractList = data['id'], data['title'], data['abstract']
    order_id = data['订单编号']
    product_name = data['宝贝名称']
    customer_name = data['买家昵称']
    comment_result = data['评价结果']
    comment_time = data['评价时间']
    comment_content = data['评价内容']
    customer = data['收货人']
    customer_phone = data['收货人手机号']
    customer_address = data['收货地区']
    wanhuishijian = data['剩余挽回时间']
    genjinren = data['跟进人']
    reason = data['原因']
    process_type = data['处理方式']
    peichang = data['赔偿金额']
    sku_pro = data['SKU属性']
    genjin_records = data['跟进记录']

    # 将所有文档输出到一个list中，一行就是一个文档
    corpus = []

    for index in range(len(comment_result)):
        # 拼接标题和摘要
        text = comment_content[index]
        text = dataPrepos(text, stopkey) # 文本预处理
        text = " ".join(text) # 连接成字符串，空格分隔
        print(text)
        corpus.append(text)

    # 1、构建词频矩阵，将文本中的词语转换成词频矩阵
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus) # 词频矩阵,a[i][j]:表示j词在第i个文本中的词频
    # 2、统计每个词的tf-idf权值
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    # 3、获取词袋模型中的关键词
    word = vectorizer.get_feature_names()
    # 4、获取tf-idf矩阵，a[i][j]表示j词在i篇文本中的tf-idf权重
    weight = tfidf.toarray()
    # 5、打印词语权重
    order_id_list = []
    product_name_list = []
    customer_name_list = []
    comment_result_list = []
    comment_time_list = []
    comment_content_list = []
    customer_list = []
    customer_phone_list = []
    customer_address_list = []
    wanhuishijian_list = []
    genjinren_list = []
    reason_list = []
    process_type_list = []
    peichang_list = []
    sku_pro_list = []
    genjin_records_list = []
    for i in range(len(weight)):
        print(u"-------这里输出第", i+1, u"篇文本的词语tf-idf------")
        order_id_list.append(order_id[i])
        product_name_list.append(product_name[i])
        customer_name_list.append(customer_name)
        comment_result_list.append(comment_result[i])
        comment_time_list.append(comment_time[i])

        customer_list.append(customer[i])
        customer_phone_list.append(customer_phone[i])
        customer_address_list.append(customer_address[i])
        wanhuishijian_list.append(wanhuishijian[i])
        genjinren_list.append(genjinren[i])
        reason_list.append(reason[i])
        process_type_list.append(process_type[i])
        peichang_list.append(peichang[i])
        sku_pro_list.append(sku_pro)
        genjin_records_list.append(genjin_records)
        df_word, df_weight = [], [] # 当前文章的所有词汇列表、词汇对应权重列表
        for j in range(len(word)):
            print(word[j], weight[i][j])
            df_word.append(word[j])
            df_weight.append(weight[i][j])
        df_word = pd.DataFrame(df_word, columns=['word'])
        df_weight = pd.DataFrame(df_weight, columns=['weight'])
        word_weight = pd.concat([df_word, df_weight], axis=1) # 拼接词汇列表和权重列表
        word_weight = word_weight.sort_values(by="weight", ascending=False) # 按照权重值降序排列
        keyword = np.array(word_weight['word']) # 选择词汇列并转成数组格式
        word_split = [keyword[x] for x in range(0, topK)] # 抽取前topK个词汇作为关键词
        word_split = " ".join(word_split)
        comment_content_list.append(word_split.encode('utf-8'))

        data_set = {
            '订单编号': order_id_list,
            '宝贝名称': product_name_list,
            '买家昵称': customer_name_list,
            '评价结果': comment_result_list,
            '评价时间': comment_time_list,
            '评价内容': comment_content_list,
            '收货人': customer_list,
            '收货人手机号': customer_phone_list,
            '收货地区': customer_address_list,
            '剩余挽回时间': wanhuishijian_list,
            '跟进人': genjinren_list,
            '原因': reason_list,
            '处理方式': process_type_list,
            '赔偿金额': peichang_list,
            'SKU属性': sku_pro_list,
            '跟进记录': genjin_records_list
        }

    result = pd.DataFrame(data_set, columns=['订单编号', '宝贝名称', '买家昵称', '评价结果', '评价时间', '评价内容', '收货人', '收货人手机号', '收货地区', '剩余挽回时间', '跟进人', '原因', '处理方式', '赔偿金额', 'SKU属性', '跟进记录'])
    return result


def main():
    # 读取数据集
    data_file = 'data/csv000.csv'
    data = pd.read_csv(data_file)
    # print(data['评价内容'])
    # for s in data['评价内容']:
    #     print(s)
    # 停用词表
    stopkey = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]
    # print(stopkey)
    # tf-idf关键词抽取
    result = getKeywords_tfidf(data, stopkey, 10)
    # result.to_csv("result/keys_TFIDF.csv", index=False)


if __name__ == '__main__':
    main()
