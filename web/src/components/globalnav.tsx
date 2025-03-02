import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "@/components/ui/navigation-menu";

import { Link } from "react-router";

import { cn } from "@/lib/utils";
import { Icon } from "@iconify/react";

function GlobalNavbar() {
  return (
    <>
      <NavigationMenu className="mx-auto flex flex-row justify-end max-w-5xl pt-4 px-4">
        <NavigationMenuList>
          <NavigationMenuItem>
            <Link to="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
              <NavigationMenuLink>Documentation 2</NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <Link to="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
              <NavigationMenuLink>Documentation</NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
    </>
  );
}

export { GlobalNavbar };
