import java.util.InputMismatchException;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class Main {

    private static final int MAX_EMPLOYEES = 40;
    private static Employee[] employees = new Employee[MAX_EMPLOYEES];
    private static int employeeCount = 0;

    //create employee object
    public static class Employee {
        String id;
        String name = "";
        int project1Score;
        int project2Score;
        int project3Score;
        String grade = "";

        //constructor for employee class. employee onject will initially be created with only adding the ID
        Employee(String id) {
            this.id = id;
        }

        // Method to calculate grade
        private String calculateGrade() {
            int average = (project1Score + project2Score + project3Score) / 3;
            if (average >= 80) return "Outstanding";
            else if (average >= 70) return "Exceeds Expectations";
            else if (average >= 40) return "Meets Expectations";
            else return "Needs Improvement";
        }
        //method used to ad employees name into the array
        public void setName(String name) {
            this.name = name;
        }

        // Method to update project scores and calculate the grade
        public void setProjectScores(int project1Score, int project2Score, int project3Score) {
            this.project1Score = project1Score;
            this.project2Score = project2Score;
            this.project3Score = project3Score;
            this.grade = calculateGrade();
        }

        public int getAverageScore() {
            return (project1Score + project2Score + project3Score) / 3;
        }



    }

    public static void main(String[] args) {
        // Main menu options stored in an array
        String[] mainMenu = {
                "Enter 0 to Exit",
                "Enter 1 to Check available vacancies",
                "Enter 2 to Register an employee",
                "Enter 3 to Delete an employee",
                "Enter 4 to Search for an employee",
                "Enter 5 to Store employee details into a file",
                "Enter 6 to Load employee details from a file",
                "Enter 7 to View the list of employees based on their names",
                "Enter 8 to View Optional controls"
        };

        // Option menu options when user enters 8
        String[] optionMenu = {
                "Enter 0 to Return to Main Menu",
                "Enter 1 to Add Employee Name",
                "Enter 2 to Add Employee Project Scores",
                "Enter 3 to Check Summary Report",
                "Enter 4 to Generate Complete Report"
        };

        // Main menu loop will run in an infinite loop till user input 0 making exit into true
        boolean exit = false;
        while (!exit) {
            int choice = displayMenu(mainMenu);

            switch (choice) {
                case 0:
                    exit = true; // Exit the program
                    System.out.println("Exiting the system...");
                    break;
                case 1:
                    checkAvailableVacancies();//the method to check the available vacancies will run here
                    break;
                case 2:
                    registerEmployee(); // method to register the employee by ID will run here
                    break;
                case 3:
                    deleteEmployee();//method to deletinng an employee will run here
                    break;
                case 4:
                    searchEmployee();
                    break;
                case 5:
                    storeEmployeeDetails();//method to upload the details in the ram to a text file
                    break;
                case 6:
                    loadEmployeeDetails();//method to get the details from an already exsisting text file
                    break;
                case 7:
                    viewEmployeeList();//method to display employees names alphabatically
                    break;
                case 8:
                    // Handle option menu
                    boolean backToMain = false;
                    while (!backToMain) {
                        int optionChoice = displayMenu(optionMenu);

                        switch (optionChoice) {
                            case 0:
                                backToMain = true; // Return to main menu
                                break;
                            case 1:
                                addEmployeeName();//ask for id then add name using selection sort
                                break;
                            case 2:
                                addEmployeeProjectScores();//askfor id then add the scores
                                break;
                            case 3:
                                checkSummaryReport();//display the total number of employees and the ones who scored more than 40
                                break;
                            case 4:
                                generateCompleteReport();//display employees from their average mark using bubble sort
                                break;
                            default:
                                System.out.println("Invalid option. Please try again.");
                        }
                    }
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }

    // Method to display menu and get user's choice while validating user input to make sure its within range of the menue and handle data type errors
    public static int displayMenu(String[] menu) {
        Scanner input = new Scanner(System.in);
        boolean valid = false;
        int choice = -1;

        while (!valid) {
            try {
                // Display the menu
                for (String menuItem : menu) {
                    System.out.println(menuItem);
                }

                // Take user input
                System.out.print("Enter your choice: ");
                choice = input.nextInt();

                // Validate the choice range
                if (choice >= 0 && choice < menu.length) {
                    valid = true; // Exit the loop if input is valid
                } else {
                    System.out.println("Invalid choice. Please enter a number between 0 and " + (menu.length - 1));
                }
            } catch (InputMismatchException e) {
                System.out.println("Input must be a number.");
                input.next(); // Clear the invalid input
            }
        }

        return choice; // Return the user's choice
    }

    // Method to register a new employee through id
    public static void registerEmployee() {
        System.out.println("Registering employee ID...");

        // Check if there is space in the array
        if (employeeCount < employees.length) {
            Scanner input = new Scanner(System.in);

            // Get employee ID from user
            System.out.print("Enter Employee ID: ");
            String id = input.nextLine();

            // Create new Employee object with ID only
            Employee newEmployee = new Employee(id);
            employees[employeeCount] = newEmployee;
            employeeCount++;

            System.out.println("Employee ID registered successfully.");
        } else {
            System.out.println("No more space to register new employees.");
        }
    }

    // Method to add employee name
    public static void addEmployeeName() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet. Please register an employee first.");
            return;
        }
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Employee ID to update name: ");
        String id = input.nextLine();

        for (Employee emp : employees) {
            if (emp != null && emp.id.equals(id)) {
                System.out.print("Enter Employee Name: ");
                emp.setName(input.nextLine());
                System.out.println("Employee name updated successfully.");
                return;
            }
        }
        System.out.println("Employee with ID " + id + " not found.");
    }

    // Method to add employee project scores
    public static void addEmployeeProjectScores() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet. Please register an employee first.");
            return;
        }
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Employee ID to update project scores: ");
        String id = input.nextLine();

        for (Employee emp : employees) {
            if (emp != null && emp.id.equals(id)) {
                int project1Score = getValidProjectScore(input, "Project 1");
                int project2Score = getValidProjectScore(input, "Project 2");
                int project3Score = getValidProjectScore(input, "Project 3");

                emp.setProjectScores(project1Score, project2Score, project3Score);
                System.out.println("Employee project scores updated successfully.");
                return;
            }
        }
        System.out.println("Employee with ID " + id + " not found.");
    }


    //used to validate the project score make sure its with in 0-100 range and then haddle data type error
    private static int getValidProjectScore(Scanner input, String projectName) {
        int score = -1;
        while (true) {
            try {
                System.out.print("Enter " + projectName + " Score (0-100): ");
                score = input.nextInt();
                if (score >= 0 && score <= 100) {
                    break; // Valid score, exit the loop
                } else {
                    System.out.println("Invalid score. Please enter a number between 0 and 100.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid integer.");
                input.next(); // Clear the invalid input
            }
        }
        return score;
    }


    // checking available vacancies
    public static void checkAvailableVacancies() {
        int availableSeats = MAX_EMPLOYEES - employeeCount;
        if (availableSeats > 0) {
            System.out.println("Available seats: " + availableSeats);
        } else {
            System.out.println("No more available seats.");
        }
    }


    public static void deleteEmployee() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet.");
            return;
        }

        Scanner input = new Scanner(System.in);
        System.out.print("Enter Employee ID to delete: ");
        String id = input.nextLine();

        for (int i = 0; i < employeeCount; i++) {
            if (employees[i] != null && employees[i].id.equals(id)) {
                // Shift remaining employees one position left to fill the gap
                for (int j = i; j < employeeCount - 1; j++) {
                    employees[j] = employees[j + 1];
                }
                employees[employeeCount - 1] = null; //remove the array last spot making iit null
                employeeCount--;
                System.out.println("Employee with ID " + id + " has been deleted.");
                return;
            }
        }
        System.out.println("Invalid ID: Employee with ID " + id + " not found.");
    }


    //search for id through a loop and then display the details. method will check if count is empty first and whether the id is correct
    public static void searchEmployee() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet.");
            return;
        }

        Scanner input = new Scanner(System.in);
        System.out.print("Enter Employee ID to search: ");
        String id = input.nextLine();

        for (Employee emp : employees) {
            if (emp != null && emp.id.equals(id)) {
                // Display employee details
                System.out.println("Employee Details:");
                System.out.println("Name: " + emp.name);
                System.out.println("Project 1 Score: " + emp.project1Score);
                System.out.println("Project 2 Score: " + emp.project2Score);
                System.out.println("Project 3 Score: " + emp.project3Score);
                System.out.println("Grade: " + emp.grade);
                return;
            }
        }
        System.out.println("Employee with ID " + id + " doesn't exist.");
    }


    //get employee details and store the to a text file through a loop access object by object then attribute by attribute will be stored
    public static void storeEmployeeDetails() {
        System.out.println("Storing employee details...");

        File file = new File("employee.txt");

        try (FileWriter writer = new FileWriter(file)) {
            for (Employee emp : employees) {
                if (emp != null) {
                    writer.write(emp.id + "," + emp.name + "," + emp.project1Score + "," + emp.project2Score + "," + emp.project3Score + "," + emp.grade);
                    writer.write(System.lineSeparator());
                }
            }
            System.out.println("Employee details stored successfully.");
        } catch (IOException e) {
            System.out.println("Error while writing to the file.");//handling errors to make sure the program doesnt crash
            e.printStackTrace();
        }
    }




    public static void loadEmployeeDetails() {
        System.out.println("Loading employee details...");

        File file = new File("employee.txt");

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            employeeCount = 0; // Reset employee count

            while ((line = reader.readLine()) != null) {//skip empty lines
                String[] parts = line.split(",");//creat an array elements split by comma
                if (parts.length == 6) {
                    String id = parts[0];
                    String name = parts[1];
                    int project1Score = Integer.parseInt(parts[2]);
                    int project2Score = Integer.parseInt(parts[3]);
                    int project3Score = Integer.parseInt(parts[4]);
                    String grade = parts[5];

                    if (employeeCount < employees.length) {
                        Employee emp = new Employee(id);
                        emp.setName(name);
                        emp.setProjectScores(project1Score, project2Score, project3Score);
                        emp.grade = grade;
                        employees[employeeCount] = emp;
                        employeeCount++;
                    }
                }
            }
            System.out.println("Employee details loaded successfully.");
        } catch (IOException e) {
            System.out.println("Error while reading the file.");
            e.printStackTrace();
        }
    }

    public static void viewEmployeeList() {
        System.out.println("Viewing list of employees...");

        if (employeeCount == 0) {
            System.out.println("No employees registered yet.");
            return;
        }

        // get only  employee names into an new array
        String[] employeeNames = new String[employeeCount];
        for (int i = 0; i < employeeCount; i++) {
            employeeNames[i] = employees[i].name;
        }

        // Perform Selection Sort on the employee names array
        for (int start = 0; start < employeeNames.length - 1; start++) {
            int minIndex = start;
            for (int i = start + 1; i < employeeNames.length; i++) {
                if (employeeNames[i].compareTo(employeeNames[minIndex]) < 0) {
                    minIndex = i;
                }
            }
            // Swap the elements
            String temp = employeeNames[start];
            employeeNames[start] = employeeNames[minIndex];
            employeeNames[minIndex] = temp;
        }

        // Display sorted names
        System.out.println("Sorted Employee Names:");
        for (String name : employeeNames) {
            System.out.println(name);
        }
    }



    public static void checkSummaryReport() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet.");
            return;
        }

        int totalRegisteredEmployees = employeeCount;
        int employeesAbove40InAllProjects = 0;

        for (Employee emp : employees) {
            if (emp != null) {
                if (emp.project1Score > 40 && emp.project2Score > 40 && emp.project3Score > 40) {
                    employeesAbove40InAllProjects++;
                }
            }
        }

        System.out.println("Summary Report:");
        System.out.println("Total Registered Employees: " + totalRegisteredEmployees);
        System.out.println("Total Employees Scoring More Than 40 in All Projects: " + employeesAbove40InAllProjects);
    }


    public static void generateCompleteReport() {
        if (employeeCount == 0) {
            System.out.println("No employees registered yet.");
            return;
        }

        // Bubble sort to sort employees by average score (descending order)
        for (int i = 0; i < employeeCount - 1; i++) {
            for (int j = 0; j < employeeCount - i - 1; j++) {
                if (employees[j] != null && employees[j + 1] != null) {
                    if (employees[j].getAverageScore() < employees[j + 1].getAverageScore()) {
                        Employee temp = employees[j];
                        employees[j] = employees[j + 1];
                        employees[j + 1] = temp;
                    }
                }
            }
        }

        // Display the complete report.
        System.out.println("Complete Employee Report:");
        for (Employee emp : employees) {
            if (emp != null) {
                System.out.println("ID: " + emp.id);
                System.out.println("Name: " + emp.name);
                System.out.println("Project 1 Score: " + emp.project1Score);
                System.out.println("Project 2 Score: " + emp.project2Score);
                System.out.println("Project 3 Score: " + emp.project3Score);
                int average = emp.getAverageScore();
                System.out.println("Average Score: " + average);
                System.out.println("Grade: " + emp.grade);
                System.out.println("------------------------");
            }
        }
    }

}
