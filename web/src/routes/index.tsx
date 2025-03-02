import { Textarea } from "@/components/ui/textarea"
import { GlobalNavbar } from "../components/globalnav";
import { Button } from "@/components/ui/button";

function Index() {
  return (
    <>
  
    <div className="bg-[url(assets/mesh-gradient.png)] bg-center bg-auto h-screen backdrop-opacity-90 backdrop-blur-md">
    <GlobalNavbar/>


    <h1 className="mt-16 scroll-m-20 text-4xl font-extrabold tracking-normal lg:text-5xl text-center">
        Insert Gene
      </h1> 
    <h3 className="mt-4 scroll-m-2 text-1xl font-extrabold tracking-normal lg:text-3xl text-center">
      yooo
    </h3>
    <div className="py-8 grid  h-3xl w-2xl gap-2  justify-self-center">
      <Textarea placeholder="Type or copy and paste your content here" />
      <Button>Analyze!</Button>
    </div>
    </div>


    </>
  );
}

export default Index;
