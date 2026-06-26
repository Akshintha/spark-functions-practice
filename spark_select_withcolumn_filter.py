from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, upper, lower, when

# Create Spark session
spark = SparkSession.builder \
    .appName("Spark Functions Practice") \
    .getOrCreate()

# Sample data
data = [
    (1, "Akshintha", "Data Analyst", 60000),
    (2, "Riya", "Business Analyst", 55000),
    (3, "John", "Data Engineer", 75000),
    (4, "Maya", "Data Analyst", 48000)
]

columns = ["id", "name", "role", "salary"]

df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()

# 1. Select specific columns
print("Select name and role:")
df.select("name", "role").show()

# 2. Select using col()
print("Select using col function:")
df.select(col("name"), col("salary")).show()

# 3. Add new column using withColumn
print("Add bonus column:")
df.withColumn("bonus", col("salary") * 0.10).show()

# 4. Add constant column
print("Add company column:")
df.withColumn("company", lit("Takeo")).show()

# 5. Convert name to uppercase
print("Uppercase names:")
df.withColumn("name_upper", upper(col("name"))).show()

# 6. Convert role to lowercase
print("Lowercase roles:")
df.withColumn("role_lower", lower(col("role"))).show()

# 7. Filter salary greater than 55000
print("Salary greater than 55000:")
df.filter(col("salary") > 55000).show()

# 8. Filter Data Analyst only
print("Only Data Analysts:")
df.filter(col("role") == "Data Analyst").show()

# 9. Add salary level using when
print("Salary level:")
df.withColumn(
    "salary_level",
    when(col("salary") >= 60000, "High")
    .otherwise("Medium")
).show()

# Stop Spark session
spark.stop()
