#e.g. 5, 5, 0, 9
#1, 1, 1, 9 or 15 for load_teacher
#7, 7, 1, 5 for sensical
# 9 for trace_data
# 15 for trace_data_new
min_edge = 2
max_edge = 2#5
min_blobs = 1
max_blobs = 9

learning_rate = 1e-3

#11 when running DRAMcopy14, load_teacher, trace_data
#5, etc. when running DRAMcopy13, load_input, create_data
glimpses = max_blobs + 1#11

#1 when running viz_count
#77 when running DRAMcopy14
#100 when running DRAMcopy13 (and 1 for viz?)
<<<<<<< HEAD
#10000 (or 9000) when running update_curves, classify_imgs2, match num_imgs
batch_size = 9000
=======
#10000 when running update_curves, classify_imgs2, match num_imgs
batch_size = 1 #77
>>>>>>> 59ac5da7889068bd5eca0fe825e7a1d7a09342e0

#change this whenever DRAM is run (before running nohup, make sure to make a directory in model_runs)
model_name = "rewrite_filterbank3_test"
