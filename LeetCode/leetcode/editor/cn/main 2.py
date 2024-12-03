# # -*- coding: utf-8 -*-
# import importlib
# import typing
# import os
#
#
# def convert_type(arg, var_type):
#     if var_type == int:
#         return int(arg)
#     elif var_type == typing.List[int]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             listing.append(int(a))
#         return listing
#     elif var_type == typing.List[typing.List[int]]:
#         listing = []
#         for a in arg[1:-1].split('],['):
#             k = []
#             for b in a.replace('[', '').replace(']', '').split(','):
#                 k.append(int(b))
#             listing.append(k)
#         return listing
#     elif var_type == typing.List[str]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             listing.append(str(a))
#         return listing
#     elif var_type == typing.List[typing.List[str]]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             k = []
#             for b in a[1:-1].split(','):
#                 k.append(str(b))
#             listing.append(k)
#         return listing
#     else:
#         return str(arg)
#
#
# def execute(qID: int, mID: int, sName='Solution'):
#     nqID = "0" * (5 - len(str(qID))) + str(qID)
#     filenames = [x for x in os.listdir('.') if x.startswith(f'LC{nqID}')]
#     if not filenames:
#         print(f"错误: 没有找到题目序号为{nqID}的python文件")
#         return
#     filename = filenames[0][: -3]
#     print(f"执行文件为: {filename}")
#
#     obj = importlib.import_module(filename)
#
#     if not hasattr(obj, sName):
#         print(f"错误: 没有{sName}类")
#         return
#     print(f"执行类名为: {sName}")
#     Solution = getattr(obj, sName)
#
#     if not hasattr(obj, 'TEST_CASE'):
#         print("错误: 没有测试案例")
#         return
#     TEST_CASE = obj.TEST_CASE
#
#     methods = [m for m in dir(Solution) if '__' not in m]
#     if not methods or mID > len(methods) - 1:
#         print(f"错误: 没有找到函数序号为{mID}的函数")
#         return
#     method = methods[mID]
#     print(f"执行函数为: {method}")
#
#     func = getattr(Solution(), method)
#     arg_count = func.__code__.co_argcount - 1
#     arg_names = func.__code__.co_varnames[1:]
#     annotation = func.__annotations__
#     cases = TEST_CASE.split()
#     if len(cases) == 0:
#         print(f"错误: 没有测试案例")
#         return
#
#     if len(cases) % arg_count != 0:
#         print(f"测试案例数目不正确，参数应有{arg_count}个，当前数据条目为{len(cases)}个")
#         return
#
#     mapper = {}
#     for i, case in enumerate(cases):
#         j = i % arg_count
#         mapper[arg_names[j]] = convert_type(case, annotation.get(arg_names[j]))
#         if j == arg_count - 1:
#             print(f"测试案例为: {mapper}\n执行结果为: {func(**mapper)}")
#
#
# if __name__ == '__main__':
#     execute(1254, 1)
