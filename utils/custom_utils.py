

class transformation:

    def dedup(df:DataFrame,dedup_cols:List,cdc:str):
        df=df.withColumn("dedupkey",concat(*dedup_cols))
        df=df.withColumn("dedupCounts",row_number().over(Window.partitionBy("dedupkey").orderBy(cdc)))
        df=df.filter(col("dedupCounts")==1)
        