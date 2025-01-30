<html>
<head>
    <title>Menu d'acceuil</title>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="accueil.css">
</head>
<body>
  <?php
      $n = $_GET['n'];
      $ln = $_GET['ln'];
      $e = $_GET['e'];

    try{
      
      $myPDO = new PDO("vos données");
    
      $sql_query1 = "INSERT INTO waiting_users(name,last_name,email)VALUES('$n', '$ln', '$e')";
      $myPDO->query($sql_query1);

    }catch (PDOException $e){
      echo $e->getMessage();
    }
  ?>
  <div class=center><p>Le nouvel utilisateur a bien été rajouté a la base de données.</p></div>
  <div class=center><a href="accueil.html"><h1>Retourner au menu.</h1></a></div>
</body>
</html>