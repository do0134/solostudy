namespace HelloCsWin
{

    public partial class Calculator : Form
    {

        private string Result_Num = "0";
        private string Start_Num = "0";
        private string lastOperator;
        private bool isStart = false;

        public Calculator()
        {
            InitializeComponent();
        }

        private void Calculator_Load(object sender, EventArgs e)
        {

        }

        private void Set_Initial()
        {
            NumScreen.Text = "0";
            isStart = true;
        }


        private void SetNum(string num)
        {
            if (isStart)
            {
                NumScreen.Text = "";
            }
            if (NumScreen.Text == Start_Num)
            {
                NumScreen.Text = num;
            }
            else
            {
                NumScreen.Text += num;
            }

            isStart = false;
        }



        private void Result_Button_Click(object sender, EventArgs e)
        {

        }

        private void NumButton_Click(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            SetNum(button.Text);
        }

        private void Calc(object sender, EventArgs e)
        {   
            if (!isStart)
            {   
                int num1 = int.Parse(Result_Num);
                int num2 = int.Parse(NumScreen.Text);

                if (lastOperator == "+")
                {
                    int result = (num1 + num2);
                    isStart = true;
                    Result_Num = result.ToString();
                } else if (lastOperator == "-")
                {
                    int result = (num1-num2);
                    isStart = true;
                    Result_Num = result.ToString();
                }

                NumScreen.Text = Result_Num;
            }

            Button operatorButton = (Button)sender;
            String Operator = operatorButton.Text;
            lastOperator = Operator;
            
        }
    }
}
