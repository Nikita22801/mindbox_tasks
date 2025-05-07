from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

# Инициализация SparkSession
spark = SparkSession.builder \
    .appName("Product-Category Relationships") \
    .getOrCreate()

# Пример данных
products_data = [
    (1, "Продукт A"),
    (2, "Продукт B"),
    (3, "Продукт C"),
    (4, "Продукт D")
]

categories_data = [
    (1, "Категория 1"),
    (2, "Категория 2"),
    (1, "Категория 3")
]

product_category_data = [
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 1)
]

# Создание датафреймов
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

def get_product_category_pairs(products_df: DataFrame, product_category_df: DataFrame) -> DataFrame:
    # Получение пар "Имя продукта - Имя категории"
    product_category_pairs = products_df.join(
        product_category_df,
        on="product_id",
        how="left"
    ).join(
        categories_df,
        on="category_id",
        how="left"
    ).select(
        "product_name",
        "category_name"
    )

    # Получение имен всех продуктов, у которых нет категорий
    no_category_products = products_df.join(
        product_category_df,
        on="product_id",
        how="left_anti"
    ).select("product_name")

    # Объединение результатов
    result = product_category_pairs.union(no_category_products.withColumn("category_name", lit(None)))

    return result

# Вызов функции
result_df = get_product_category_pairs(products_df, product_category_df)

# Показать результат
result_df.show(truncate=False)
