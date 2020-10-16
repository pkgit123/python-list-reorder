# original list of columns in S3 and Redshift
ls_cols_csv_s3 = ['C3', 'E5', 'A1', 'D4', 'B2']
ls_cols_Redshift = ['a_1', 'b_2', 'c_3', 'd_4', 'e_5']

print("Original column names, similar, incorrect order.")
print("ls_cols_csv_s3: ", ls_cols_csv_s3)
print("ls_cols_Redshift: ", ls_cols_Redshift)
print()

# step 1: copy list of s3 columns, to cleanse for comparison
ls_copy_cols_csv_s3 = ls_cols_csv_s3.copy()
ls_copy_cols_csv_s3 = [x.lower() for x in ls_copy_cols_csv_s3]
ls_copy_cols_csv_s3 = [x.replace('_', "") for x in ls_copy_cols_csv_s3]

# step 2: copy list of Redshift columns, to cleanse for comparison
ls_copy_cols_Redshift = ls_cols_Redshift.copy()
ls_copy_cols_Redshift = [x.lower() for x in ls_copy_cols_Redshift]
ls_copy_cols_Redshift = [x.replace('_', "") for x in ls_copy_cols_Redshift]

print("Cleansed lists, identical, incorrect order.")
print("ls_copy_cols_csv_s3: ", ls_copy_cols_csv_s3)
print("ls_copy_cols_Redshift: ", ls_copy_cols_Redshift)
print()

# step 3: make sure the lists are identical, except for order
print("make sure the lists are identical, except for order: ", set(ls_copy_cols_csv_s3)==set(ls_copy_cols_Redshift))
print()

# step 4: list of reorder index from s3 to Redshift
ls_reorder_s3_to_redshift = [ls_copy_cols_csv_s3.index(i) for i in ls_copy_cols_Redshift]

# step 5: create list of reordered items in s3 to match Redshift
ls_s3_correct_order = [ls_copy_cols_csv_s3[i] for i in ls_reorder_s3_to_redshift]

# step 6: verify the orders match
print("Original column names, similar, correct order.")
print("ls_s3_correct_order: ", ls_s3_correct_order)
print("ls_cols_Redshift: ", ls_cols_Redshift)
