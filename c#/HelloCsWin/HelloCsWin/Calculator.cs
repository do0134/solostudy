namespace HelloCsWin
{
    public partial class Calculator : Form
    {
        public Calculator()
        {
            InitializeComponent();
        }

        private void Calculator_Load(object sender, EventArgs e)
        {

        }

        private void HelloLabel_Click(object sender, EventArgs e)
        {
            int number1 = 10;
            int number2 = 20;
            int sum = number1 + number2;
            HelloLabel.Text = sum.ToString();

        }

        private void SumNumbers_Click(object sender, EventArgs e)
        {

            int? number1 = checkValidNumber(SumInput1.Text);
            int? number2 = checkValidNumber(SumInput2.Text);

            if (number1.HasValue && number2.HasValue)
            {
                int sum = Add(number1.Value, number2.Value);
                SumResult.Text = sum.ToString();
            } else
            {
                MessageBox.Show("올바른 숫자를 입력해주세요");
                return;
            }            
        }

        private int Add(int number1, int number2)
        {
            int sum = number1 + number2;
            return sum;
        }

        private float Add(float number1, float number2) { 
            float sum = number1 + number2;
            return sum;
        }

        private int? checkValidNumber(String number)
        {
            int validNumber = 0;
            if (String.IsNullOrWhiteSpace(number) | !int.TryParse(number, out validNumber)) {
                return null;
            }

            return validNumber;
        }

    }
}
