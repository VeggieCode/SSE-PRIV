from django.db import migrations

sql_query = ("INSERT INTO `student_module_estados` VALUES (1,'01','Aguascalientes','Ags.',1),(2,'02',"
             "'Baja California','BC',1),(3,'03','Baja California Sur','BCS',1),(4,'04','Campeche','Camp.',1),(5,'05',"
             "'Coahuila de Zaragoza','Coah.',1),(6,'06','Colima','Col.',1),(7,'07','Chiapas','Chis.',1),(8,'08',"
             "'Chihuahua','Chih.',1),(9,'09','Ciudad de México','CDMX',1),(10,'10','Durango','Dgo.',1),(11,'11',"
             "'Guanajuato','Gto.',1),(12,'12','Guerrero','Gro.',1),(13,'13','Hidalgo','Hgo.',1),(14,'14','Jalisco',"
             "'Jal.',1),(15,'15','México','Mex.',1),(16,'16','Michoacán de Ocampo','Mich.',1),(17,'17','Morelos',"
             "'Mor.',1),(18,'18','Nayarit','Nay.',1),(19,'19','Nuevo León','NL',1),(20,'20','Oaxaca','Oax.',1),(21,"
             "'21','Puebla','Pue.',1),(22,'22','Querétaro','Qro.',1),(23,'23','Quintana Roo','Q. Roo',1),(24,'24',"
             "'San Luis Potosí','SLP',1),(25,'25','Sinaloa','Sin.',1),(26,'26','Sonora','Son.',1),(27,'27','Tabasco',"
             "'Tab.',1),(28,'28','Tamaulipas','Tamps.',1),(29,'29','Tlaxcala','Tlax.',1),(30,'30','Veracruz de "
             "Ignacio de la Llave','Ver.',1),(31,'31','Yucatán','Yuc.',1),(32,'32','Zacatecas','Zac.',1)")


class Migration(migrations.Migration):
    dependencies = [
        ('student_module', '0002_add_licenciaturas'),
    ]

    operations = [
        migrations.RunSQL(sql=sql_query)
    ]
