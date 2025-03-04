import java.util.*;

class Module {
    private String moduleName;
    private int moduleMark;

    public Module(String moduleName) {
        this.moduleName = moduleName;
        this.moduleMark = 0;
    }

    public String getModuleName() {
        return moduleName;
    }

    public void setModuleName(String moduleName) {
        this.moduleName = moduleName;
    }

    public int getModuleMark() {
        return moduleMark;
    }

    public void setModuleMark(int moduleMark) {
        this.moduleMark = moduleMark;
    }

    @Override
    public String toString() {
        return moduleName + ": " + moduleMark;
    }
}

class Student {
    private String studentID;
    private String studentName;
    private Module[] modules;
    private String moduleGrade;

    public Student(String studentID, String studentName) {
        this.studentID = studentID;
        this.studentName = studentName;
        this.modules = new Module[]{new Module("Module1"), new Module("Module2"), new Module("Module3")};
        this.moduleGrade = "N/A";
    }

    public String getStudentID() {
        return studentID;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public Module[] getModules() {
        return modules;
    }

    public void setModuleMarks(int module1, int module2, int module3) {
        this.modules[0].setModuleMark(module1);
        this.modules[1].setModuleMark(module2);
        this.modules[2].setModuleMark(module3);
        calculateGrade();
    }

    public double getAverageMarks() {
        return (modules[0].getModuleMark() + modules[1].getModuleMark() + modules[2].getModuleMark()) / 3.0;
    }

    public int getTotalMarks() {
        return modules[0].getModuleMark() + modules[1].getModuleMark() + modules[2].getModuleMark();
    }

    private void calculateGrade() {
        double average = getAverageMarks();
        if (average >= 80) {
            this.moduleGrade = "Distinction";
        } else if (average >= 70) {
            this.moduleGrade = "Merit";
        } else if (average >= 40) {
            this.moduleGrade = "Pass";
        } else {
            this.moduleGrade = "Fail";
        }
    }

    public String toFileString() {
        return studentID + "," + studentName + "," + modules[0].getModuleMark() + "," + modules[1].getModuleMark() + "," + modules[2].getModuleMark();
    }

    public static Student fromFileString(String line) {
        String[] parts = line.split(",");
        Student student = new Student(parts[0], parts[1]);
        student.setModuleMarks(Integer.parseInt(parts[2]), Integer.parseInt(parts[3]), Integer.parseInt(parts[4]));
        return student;
    }

    @Override
    public String toString() {
        return "Student ID: " + studentID + "\nName: " + studentName + "\nModules: " + Arrays.toString(modules) + "\nGrade: " + moduleGrade + "\n";
    }
}

public class Main {
    private static ArrayList<Student> students = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Register Student\n2. Enter Student Results\n3. View Students\n4. Exit");
            System.out.print("Enter choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter student ID: ");
                    String studentID = scanner.nextLine();
                    System.out.print("Enter student name: ");
                    String studentName = scanner.nextLine();
                    students.add(new Student(studentID, studentName));
                    break;
                case 2:
                    System.out.print("Enter student ID: ");
                    String id = scanner.nextLine();
                    Student student = findStudentByID(id);
                    if (student != null) {
                        System.out.print("Enter marks for Module 1: ");
                        int m1 = scanner.nextInt();
                        System.out.print("Enter marks for Module 2: ");
                        int m2 = scanner.nextInt();
                        System.out.print("Enter marks for Module 3: ");
                        int m3 = scanner.nextInt();
                        student.setModuleMarks(m1, m2, m3);
                    } else {
                        System.out.println("Student not found.");
                    }
                    break;
                case 3:
                    for (Student s : students) {
                        System.out.println(s);
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    private static Student findStudentByID(String studentID) {
        for (Student student : students) {
            if (student.getStudentID().equals(studentID)) {
                return student;
            }
        }
        return null;
    }
}
