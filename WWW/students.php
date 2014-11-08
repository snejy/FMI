<?php
require 'config.php';
include_once(LIB.'/student.php');

class Students {
    function findAll($limit = 10, $orderby = "fn DESC"){
        try{
            $dbs = new PDO('mysql:host='. DB_SERVER.';dbname='.DB_NAME, DB_USERNAME, DB_PASSWORD);
                $ret = array();
                foreach($dbs->query('SELECT * FROM students ORDER BY' . $orderby .' LIMIT'. $limit) as $row) {
                    $ret[] = new Student($row['id'], $row['fn'], $row['first_name'], $row['last_name'], $row['major'], $row['grade']);
                }
                return $ret;
                $dbs = null;
        } catch (PDOException $e) {
            print "Error!: " . $e->getMessage() . "<br/>";
            die();
        }
    }

    function getStudentsData() {
        try{
            $dbs = new PDO('mysql:host='. DB_SERVER.';dbname='.DB_NAME, DB_USERNAME, DB_PASSWORD);
                $ret = array();
                foreach($dbs->query('SELECT * FROM students ORDER BY grade DESC LIMIT 10') as $row) {
                    $ret[] = $row;
                }
                return $ret;
                $dbs = null;
        } catch (PDOException $e) {
            print "Error!: " . $e->getMessage() . "<br/>";
            die();
            }
    }

    function insertNewStudent($student_data){
        try{
            $dbs = new PDO('mysql:host='. DB_SERVER.';dbname='.DB_NAME, DB_USERNAME, DB_PASSWORD);
            foreach($dbs->query('SELECT * FROM students WHERE fn LIKE '. $student_data['fn'] ) as $row) {
                if($row){
                    $dbs->beginTransaction();
                    $sql = 'UPDATE students SET first_name = :fname, last_name = :lname, major = :major, grade = :grade, last_updated = :updated WHERE fn = :fn';
                    $statement = $dbs->prepare($sql);
                    $statement->execute(array(':fname' => $student_data['first_name'], ':lname' => $student_data['last_name'],':major' => $student_data['major'],':grade' => $student_data['grade'],':updated' => '30-10-2014', ':fn' => $student_data['fn']));
                    $dbs->commit();
                }
            }
            if(!$row){
                $dbs->beginTransaction();
                $sql = "INSERT INTO students(first_name, last_name, major, grade, last_updated, fn)
                    VALUES(:fname, :lname, :major, :grade, :updated, :fn)";
                $statement = $dbs->prepare($sql);
                $statement->execute(array(':fname' => $student_data['first_name'], ':lname' => $student_data['last_name'],':major' => $student_data['major'],':grade' => $student_data['grade'],':updated' => '30-10-2014', ':fn' => $student_data['fn']));
                $dbs->commit();
            }
        } catch (PDOException $e) {
            print "Error!: " . $e->getMessage() . "<br/>";
            die();
            }
    }
}
    
?>