import java.io.File;
import java.io.FileInputStream;
public class problem1 {
    public static void main(String[] args) {
        {
            try
            {
                //constructor of file class having file as argument
                File file = new File(".\\test.txt");
                FileInputStream fis = new FileInputStream(file);     //opens a connection to an actual file
                System.out.println("file content: ");
                int r = 0;                                          //byte of data read
                byte[] line = new byte[6];
                int val = 0b0;
                while((r = fis.read())!=-1)
                {
                    if (r == 13) {
                        continue;
                    }
                    if (r == 10) {
                        val >>>= 1;
                        System.out.println(Integer.toBinaryString(val));
                        val = 0b0;
                    }
                    val += r == 49 ? 0b1 : 0b0;
                    val <<= 1;
//                    System.out.print(val);
//                    System.out.println(r);      //prints the content of the file
                }
            }
            catch(Exception e)
            {
                e.printStackTrace();
            }
        }
    }
}
