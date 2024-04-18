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
    }
}
