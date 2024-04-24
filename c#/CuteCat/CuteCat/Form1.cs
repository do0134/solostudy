namespace CuteCat
{
    public partial class Form1 : Form
    {

        private Cat MyCat = new Cat("æﬂøÀ¿Ã", 1);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Play_Click(object sender, EventArgs e)
        {
            MyCat.Play();
            CatScreen.Text = MyCat.Express();
        }

        private void Feed_Click(object sender, EventArgs e)
        {
            MyCat.Eat();
            CatScreen.Text = MyCat.Express();
        }

        private void Cat_GetBoard(object sender, EventArgs e)
        {
            MyCat.GetBored();
            CatScreen.Text = MyCat.Express();
        }
    }


}
