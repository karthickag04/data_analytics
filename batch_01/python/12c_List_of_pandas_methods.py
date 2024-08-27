
# Pandas DataFrame Manipulation Methods

# 1. df.head() - Return the first n rows.
# 2. df.tail() - Return the last n rows.
# 3. df.info() - Concise summary of a DataFrame.
# 4. df.describe() - Generate descriptive statistics.
# 5. df.shape - Return a tuple representing the dimensionality of the DataFrame.
# 6. df.columns - Return the column labels of the DataFrame.
# 7. df.index - Return the index (row labels) of the DataFrame.
# 8. df.dtypes - Return the data types of the columns.
# 9. df.T - Transpose the DataFrame.
# 10. df.sort_values() - Sort the DataFrame by the values of one or more columns.
# 11. df.sort_index() - Sort the DataFrame by index labels.
# 12. df.rename() - Alter axes labels (index or columns).
# 13. df.set_index() - Set the DataFrame’s index (row labels).
# 14. df.reset_index() - Reset the index of the DataFrame.
# 15. df.drop() - Drop specified labels from rows or columns.
# 16. df.dropna() - Remove missing values.
# 17. df.fillna() - Fill missing values.
# 18. df.isna() - Detect missing values.
# 19. df.notna() - Detect existing (non-missing) values.
# 20. df.duplicated() - Return boolean Series denoting duplicate rows.
# 21. df.drop_duplicates() - Remove duplicate rows.
# 22. df.value_counts() - Return a Series containing counts of unique values.
# 23. df.unique() - Return unique values of Series.
# 24. df.nunique() - Count distinct observations over requested axis.
# 25. df.apply() - Apply a function along an axis of the DataFrame.
# 26. df.applymap() - Apply a function to a DataFrame elementwise.
# 27. df.map() - Map values of Series according to an input mapping.
# 28. df.groupby() - Group DataFrame using a mapper or by series of columns.
# 29. df.agg() - Aggregate using one or more operations over the specified axis.
# 30. df.transform() - Apply a function that returns a like-indexed DataFrame.
# 31. df.corr() - Compute pairwise correlation of columns.
# 32. df.cov() - Compute pairwise covariance of columns.
# 33. df.mean() - Return the mean of the values over the requested axis.
# 34. df.median() - Return the median of the values over the requested axis.
# 35. df.mode() - Get the mode(s) of each element along the selected axis.
# 36. df.sum() - Return the sum of the values over the requested axis.
# 37. df.min() - Return the minimum of the values over the requested axis.
# 38. df.max() - Return the maximum of the values over the requested axis.
# 39. df.std() - Return sample standard deviation over the requested axis.
# 40. df.var() - Return unbiased variance over the requested axis.
# 41. df.mad() - Return the mean absolute deviation over the requested axis.
# 42. df.skew() - Return sample skewness over the requested axis.
# 43. df.kurt() - Return sample kurtosis over the requested axis.
# 44. df.rank() - Compute numerical data ranks along axis.
# 45. df.pivot() - Reshape data (produce a “pivot” table) based on column values.
# 46. df.pivot_table() - Create a spreadsheet-style pivot table as a DataFrame.
# 47. df.str.contains() - Check if string values contain a specific substring.
# 48. df.str.replace() - Replace occurrences of a string pattern in the DataFrame.
# 49. df.str.extract() - Extract a substring matching a regular expression pattern.
# 50. df.str.split() - Split strings into lists or separate columns.
# 51. df.str.lower() / df.str.upper() - Convert strings to lower or upper case.
# 52. pd.to_datetime() - Convert argument to datetime.
# 53. df.dt.year / df.dt.month / df.dt.day - Access year, month, day from datetime.
# 54. df.resample() - Resample time-series data.
# 55. df.tz_localize() - Localize tz-naive timestamps to a timezone.
# 56. df.tz_convert() - Convert timestamps to another time zone.
# 57. df.cumsum() - Compute cumulative sum.
# 58. df.cumprod() - Compute cumulative product.
# 59. df.cummax() - Compute cumulative maximum.
# 60. df.cummin() - Compute cumulative minimum.
# 61. df.diff() - Calculate the difference between rows or columns.
# 62. df.pct_change() - Compute percentage change between rows or columns.
# 63. df.rolling() - Provide rolling window calculations.
# 64. df.expanding() - Provide expanding window calculations.
# 65. df.ewm() - Exponentially weighted moving window calculations.
# 66. df.astype('category') - Convert a column to a categorical type.
# 67. df.cat.categories - Get or set the categories of a categorical column.
# 68. df.cat.codes - Get codes of the categories in a categorical column.
# 69. df.cat.add_categories() - Add new categories to an existing categorical column.
# 70. df.cat.remove_unused_categories() - Remove unused categories from a categorical column.
# 71. pd.SparseDataFrame() - Create a DataFrame optimized for sparse data.
# 72. df.to_sparse() - Convert a DataFrame to a sparse DataFrame.
# 73. df.sparse.density - Calculate the density (non-sparse elements) of the DataFrame.
# 74. df.set_index([cols]) - Set multiple columns as the index.
# 75. df.swaplevel() - Swap levels of a MultiIndex.
# 76. df.stack(level=-1) - Stack the prescribed level(s) from columns to index.
# 77. df.unstack(level=-1) - Unstack the prescribed level(s) from index to columns.
# 78. df.reorder_levels() - Rearrange levels of a MultiIndex.
# 79. df.sparse.to_dense() - Convert a sparse DataFrame back to a dense format.
# 80. df.sparse.density - Check the density of the DataFrame (ratio of non-zero to total elements).
# 81. df.to_csv() - Write DataFrame to a CSV file.
# 82. df.to_excel() - Write DataFrame to an Excel file.
# 83. pd.read_csv() - Read a CSV file into a DataFrame.
# 84. pd.read_excel() - Read an Excel file into a DataFrame.
# 85. df.to_sql() - Write records stored in a DataFrame to a SQL database.
# 86. pd.read_sql() - Read a SQL query or database table into a DataFrame.
# 87. df.to_json() - Convert the DataFrame to a JSON string.
# 88. pd.read_json() - Read a JSON string into a DataFrame.
# 89. df.plot() - Generate plots from DataFrame data.
# 90. df.hist() - Plot histograms of DataFrame columns.
# 91. df.boxplot() - Create box plots from DataFrame columns.
# 92. df.scatter_matrix() - Plot a matrix of scatter plots.
# 93. df.plot.bar() - Create bar plots from DataFrame data.
# 94. df.plot.line() - Create line plots from DataFrame data.
# 95. df.plot.pie() - Create pie charts from DataFrame data.
# 96. df.sample() - Randomly sample rows or columns from a DataFrame.
# 97. df.memory_usage() - Return the memory usage of each column.
# 98. df.clip() - Trim values at input thresholds.
# 99. df.idxmax() - Return the index of the first occurrence of the maximum over a requested axis.
# 100. df.idxmin() - Return the index of the first occurrence of the minimum over a requested axis.
# 101. df.lookup() - Label-based "fancy indexing" for selection by row/column pairs.
# 102. df.align() - Align two objects on their axes with the specified join method.
# 103. df.reindex() - Change the row labels (index) and/or column labels of the DataFrame.
# 104. df.where() - Replace elements not meeting the condition with a specified value.
# 105. df.mask() - Replace elements meeting the condition with a specified value.
# 106. df.rolling() - Provides rolling window calculations.
# 107. df.expanding() - Provides expanding window calculations.
# 108. df.ewm() - Provides exponentially weighted window calculations.
# 109. pd.SparseDataFrame() - Create a DataFrame optimized for sparse data storage.
# 110. df.to_dense() - Convert a sparse DataFrame to a dense one.
# 111. df.sparse.from_spmatrix() - Create a DataFrame from a sparse matrix.
# 112. df.memory_usage(deep=True) - Get the memory usage of a DataFrame, 
