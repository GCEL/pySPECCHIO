package testpkg;

public class Test {
  private String msg;

  public Test() {
    msg = "nothing so far...";
  }

  public static void speak(String msg) {
    System.out.println(msg);
  }

  public void setString(String s) {
    msg = s;
  }

  public String getString() {
    return msg;
  }
}
