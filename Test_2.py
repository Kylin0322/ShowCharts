
import file_op

file_list = file_op.get_file_list(r"C:\TestLogSummary\UPH")
print(file_list)

l1 = file_op.file_list_filiter(file_list, act1="keep", str1="cnhuahpict12")

print("=========================================")
print(l1)
