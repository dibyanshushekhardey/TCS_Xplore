/* 
Create a class Employee with below attributes:

employeeId - int
employeeName - String
age - int
gender - char
salary - double

where employeeId is the unique identifier of the employee, employeeName is the name of the employee, age is the age of 
the employee, gender is the gender of the employee and salary is the salary of the employee.

The above attributes should be private, write getters, setters and parameterized constructor as required.

Create class Solution with main method.
Implement two static methods - getEmployeeWithSecondLowestSalary and countEmployeesBasedOnAge in Solution class.

getEmployeeWithSecondLowestSalary method:
This method will take an array of Employee objects as a parameter.
The method will return the Employee object with the second lowest salary in the array of Employee objects.
If there are less than two employees in the array, then the method should return null.

countEmployeesBasedOnAge method:
This method will take two input parameters - array of Employee objects and an integer parameter (for age).
The method will return the count of employees from the array of Employee objects whose age matches with the input 
parameter.
If no employee with the given age is present in the array of Employee objects, then the method should return 0.

Note :

Two employee objects can have the same salary.
All the searches should be case insensitive.

The above mentioned static methods should be called from the main method.

For getEmployeeWithSecondLowestSalary method - The main method should print the employeeId followed by # and employeeName
from the returned Employee object, if the returned value is not null.

If the returned value is null then it should print "Null".

For countEmployeesBasedOnAge method - The main method should print the count of employees as it is, if the returned value
is greater than 0, otherwise it should print "No employee found for the given age".

Before calling these static methods in main, use Scanner to read the number of objects and objects to read the values of 
Employee objects referring attributes in the above mentioned attribute sequence.

Consider below sample input and output:

Input:
-------------
4
101
John
30
M
10000.00
102
Samantha
25
F
15000.00
103
Alex
28
M
12000.00
104
Lisa
30
F
15000.00
30

Output:
----------------
103#Alex
2 
*/
import java.util.*;

public class Solution{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt(); sc.nextLine();
        Employee [] arr = new Employee[size];
        for(int i = 0; i < size; i++){
            int a = sc.nextInt(); sc.nextLine();
            String b = sc.nextLine();
            int c = sc.nextInt(); sc.nextLine();
            char d = sc.next().charAt(0); sc.nextLine();
            int e = sc.nextInt(); sc.nextLine();
            arr[i]=new Employee(a, b, c, d, e);
        }
        int age_input = sc.nextInt();

        Employee[] ans1 = getEmployeeWithSecondLowestSalary(arr);
        if (ans1 != null){
            for(int i = 0; i < ans1.length; i++){
                System.out.println(ans1[i].getEmployeeId()+"#"+ans1[i].getEmployeeName());
            }
        }
        else{
            System.out.print("Null");
        }

        int ans2 = countEmployeesBasedOnAge(arr, age_input);
        if(ans2!=0){
            System.out.println(ans2);
        }
        else{
            System.out.println("No employee found for the given age");
        }



    }

    public static Employee[] getEmployeeWithSecondLowestSalary(Employee[] arr){
        Employee[] det = new Employee[0];
        if(arr.length>1){
            for(int i = 0; i < arr.length; i++){
                for(int j = 0; j < arr.length; j++){
                    if(arr[i].getSalary() > arr[j].getSalary()){
                        Employee k = arr[i];
                        arr[i] = arr[j];
                        arr[j] = k;
                    }
                }
            }
            //Employee min = arr[0];
            for(int i = 0; i <arr.length; i++){
                if(arr[i].getSalary() > arr[0].getSalary()){
                    det = Arrays.copyOf(det, det.length+1);
                    det[det.length - 1]=arr[i];
                    break;
                }
            }
            for(int i = 0; i < arr.length; i++){
                if(det[0].getSalary()==arr[i].getSalary() && arr[i].getEmployeeId() != det[0].getEmployeeId()){
                    det = Arrays.copyOf(det, det.length+1);
                    det[det.length-1] = arr[i];
                }
            }
            return det;
        }
        return null;
    }

    public static int countEmployeesBasedOnAge(Employee [] arr, int age_input){
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            if (arr[i].getAge() == age_input){
                count++;
            }
        }
        return count;

    }


}
class Employee{
    int employeeId;
    String employeeName;
    int age;
    char gender;
    double salary;

    // parameter
    public Employee (int employeeId, String employeeName, int age, char gender, double salary){
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.age = age;
        this.gender = gender;
        this.salary = salary;
    }

    // getters
    public int getEmployeeId(){
        return employeeId;
    }
    public String getEmployeeName(){
        return employeeName;
    }
    public int getAge(){
        return age;
    }
    public char getGender(){
        return gender;
    }
    public double getSalary(){
        return salary;
    }

    // setters
    public void setEmployeeId(int employeeId){
        this.employeeId=employeeId;
    }
    public void setEmployeeName(String employeeName){
        this.employeeName=employeeName;
    }
    public void setAge(int age){
        this.age=age;
    }
    public void setGender(char gender){
        this.gender=gender;
    }
    public void setSalary(double salary){
        this.salary=salary;
    }
    

}