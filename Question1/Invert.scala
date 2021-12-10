import org.apache.spark
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.functions.explode
import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import scala.collection.mutable.ArrayBuffer
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.Encoder
import org.apache.spark.sql.Encoders
import org.apache.spark.sql.SparkSession


object Bestiaire extends App{
  //Execution commence ici
  val conf = new SparkConf().setAppName("Bestiaire").setMaster("local[*]")
  val sc = new SparkContext(conf)

  val spark = SparkSession
    .builder()
    .appName("Bestiaire")
    .config(conf)
    .getOrCreate()

  sc.setLogLevel("ERROR")
  import spark.implicits._

  case class Creature(title : String, spells : ArrayBuffer[String])
  case class Sort (tittle : String, monster : String)

  val path = "src/main/resources/bestiaire.json"

  val bestiaireDS = spark.read.json(path).as[Creature].rdd
  //bestiaireDS.collect().foreach(println)

  def Invert(c : Creature) : ArrayBuffer[(String, String)] = {
    val inverted = new ArrayBuffer[(String, String)]()

    for(sort <- c.spells){
      inverted += ((sort, c.title + "; "))
    }

    return inverted
  }


  val invertedDS = bestiaireDS.flatMap(x => Invert(x)).reduceByKey((a, b) => a + b)

  invertedDS.collect().foreach(println)

  invertedDS.toDF().write.json("src/main/resources/out_json")



}
