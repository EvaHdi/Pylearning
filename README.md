# Pylearning
"""
主要是进行Python的学习
近期学习任务 Python正则表达式和网络编程
持续更新中
"""
最新更新





```python
magicApi = Oakgate_At4_Generator(excel_config_abspath,
                                    at4_output_absdir)
# 传入excel路径和输出at4的路径，实例化一个Oakgate_At4_Generator类
# 会执行一些init代码，包括创建各种文件夹，保存所有日志输出信息，实例化一个EXCEL_API类，用于后续操作

# 调用parse_excel_config_file进行生成流程，传入最大测试时间和测试等级
magicApi.parse_excel_config_file(total_test_time=3600, test_level=TEST_LEVEL.STAGE_LOW)

# 循环来处理对应的Template，如"IO-PRPs" "Reset" 
self.xmlApi = XML_API(self.base_at4_abspath,self.log)
# 初始化一个XML_API的实例，用于后续操作XML

self.parse_excel_config_sheet(sheet_index=sheet_index,
                              sheet_name=sheet_name,

# 通过excel_api.get_all_rows来获取excel中的数据并分为几个列表存入
group_row_list = self.excel_api.get_all_rows(self.sheet_index, 1)
self.log.logging_info("group_row_list:{}\n".format(group_row_list))
property_row_list = self.excel_api.get_all_rows(self.sheet_index, 2)
self.log.logging_info("property_row_list:{}\n".format(property_row_list) )
domain_row_list = self.excel_api.get_all_rows(self.sheet_index, 4)
self.log.logging_info("domain_row_list:{}\n".format(domain_row_list))
default_value_row_list = self.excel_api.get_all_rows(self.sheet_index, 5)
self.log.logging_info("default_value_row_list:{}\n".format(default_value_row_list) )

# 通过循环，将所有的值存入group_dict，同时也会储存默认值
# 使用self.gen_default_oakcfg_bysheet()函数生成Default.oakcfg
self.gen_default_oakcfg_bysheet(sheet_name, default_value_dict)
# 生成oakcfg地址后传入JSON_API,用于生成json_config实例，调用实例的writeall函数写入模板cfg，从而生成新的cfg
                 
# 调用value_itear_comb随机生成测试数据以便插入后续的at4中
# 这里主要是使用python的内置函数，每组里面随机挑一个组成，重复率为1，只允许出现一次，最后返回一个combination_list
combination_list = self.value_itear_comb(test_level=test_level,share_property=group_dict[group_name_item]['Propery'],data_list=member_list)
                              
# 调用每一个的生成函数如下，最后生成一个oakcfg_dict最终再传入下个函数生成oakcfg
if  "group_dict_IO-Queue" == group_name_item:
     domain_name_list = group_dict[group_name_item]["domain_name_list"]
     gen_status =self.gen_ioqueue_group(self.sheet_name,group_name,domain_name_list, combination_list)
     self.log.logging_info("{} status={}".format(group_name, gen_status)) 
                                                         
# 调用get_oak_lun_settings(isLatest=True)获得默认cfg里的lunsetting的参数
lunStatus, default_pattern_text = self.get_oak_lun_settings(isLatest=True)
                              
# 每个函数里都会调用self.gen_oakcfg_config_case来生成oakcfg
self.gen_oakcfg_config_case(sheet_name, group_name, comb_count, oakcfg_dict)
                              
# 先用默认的lunsetting生成at4后，使用循环找到要修改的参数，进行修改 使用set_new_at4_lunsettings
self.set_new_at4_lunsettings(sheet_name, group_name, comb_count, new_pattern_text)  
                              
# 在set_new_at4_lunsettings里调用 self.xmlApi.UpdateKeyTree()进行更新
                              
# set_new_at4_lunsettings中调用XML_API的SaveXML方法保存
                              
# 其他生成方法一样，最后所有的at4生成完成后还会调用gen_default_oakcfg_bysheet来生成最后一个config_all_Default.oakcfg，就是将self.all_value_default_dict，全部写入
```

