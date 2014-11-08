<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title> Students </title>
    </head>
    <body>

        <?php
        require 'config.php';


        class Student{

            private $id;
            private $fn;
            private $first_name;
            private $last_name;
            private $major;
            private $grade;

            function __constuct($id, $fn, $first_name, $last_name, $major, $grade){
                $this->id = $id;
                $this->fn = $fn;
                $this->first_name = $first_name;
                $this->last_name = $last_name;
                $this->major = $major;
                $this->grade = $grade;
            }

            public function setFirstName($name) {
                  $this->first_name = $name;
            }

            public function getFirstName() {
                  return $this->first_name;
            }

            public function setLastName($name) {
                  $this->last_name = $name;
            }

            public function getLastName() {
                  return $this->last_name;
            }

            public function setId($id_name) {
                  $this->id = $id_name;
            }

            public function getId() {
                  return $this->id;
            }

            public function setFn($fnname) {
                  $this->fn = $fnname;
            }

            public function getFn() {
                  return $this->fn;
            }

            public function setMajor($name) {
                  $this->major = $name;
            }

            public function getMajor(){
                  return $this->major;
            }

            public function setGrade($name) {
                  $this->grade = $name;
            }

            public function getGrade() {
                  return $this->grade;
            }

            function save(){
                insertNewStudent(array('fn' => $this.$fn, 'first_name' => $this.$first_name,'last_name' => $this.$last_name, 'major' => $this.$major, 'grade' => $this.$grade));
            }

            function delete(){
                try{
                    $dbs = new PDO('mysql:host='. DB_SERVER.';dbname='.DB_NAME , DB_USERNAME, DB_PASSWORD);
                    $dbs->beginTransaction();
                    $sql = 'DELETE FROM students WHERE id = :id';
                    $statement = $dbs->prepare($sql);
                    $statement->execute(array(':id' => $this.$id));
                    $dbs->commit();
                } catch (PDOException $e) {
                    print "Error!: " . $e->getMessage() . "<br/>";
                    die();
                }
            }

            function find($fn){
            try{
                $dbs = new PDO('mysql:host='. DB_SERVER.';dbname='.DB_NAME, DB_USERNAME, DB_PASSWORD);
                foreach($dbs->query('SELECT * FROM students WHERE fn LIKE '. $fn ) as $row) {
                    if($row){
                        $obj = new Student($row['id'], $row['fn'], $row['first_name'], $row['last_name'], $row['major'],   $row['grade']);
                        return $obj;
                        $dbs = null;    
                    }
                }
            } catch (PDOException $e) {
                print "Error!: " . $e->getMessage() . "<br/>";
                die();
                }
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

        $toInsert = array(
          array('fn' => '61556', 'first_name' => 'Ivan','last_name' => 'Ivanov', 
                  'major' => 'Computer science', 'grade' => 5.45),
          array('fn' => '811546', 'first_name' => 'Peter', 'last_name' => 'Petrov',
                      'major' => 'Computer science', 'grade' => 3.45),
          array('fn' => '61556', 'first_name' => 'Ivan', 'last_name' => 'Ivanov',
                      'major' => 'Computer science', 'grade' => 4.80));

        foreach($toInsert as $record){
            insertNewStudent($record);
        }

        $data['students'] = getStudentsData();

        if (sizeof($data['students']) == 0) {
            echo 'Error. The database is empty.';
        }
        ?>

        <table border='1'>
            <tr><th>Statistics</th></tr>
            <?php
            if($data['students']) {
                foreach ($data['students'] as $student) {
                    echo '<tr><td>' . $student['fn'] . ' - ' . $student['first_name'] . ' - ' .
                     $student['last_name'] . ' - '. $student['grade'] . ' - major: ' . $student['major'] .  '</td></tr>';
                    }
                }
            ?>
        </table>
    </body>
</html>