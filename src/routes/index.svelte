<script lang="ts">
  import {
    Alert,
    Avatar,
    AvatarGroup,
    AvatarGroupCounter,
    Badge,
    Breadcrumb,
    BreadcrumbItem,
    Button,
    Card,
    Tooltip,
    Dropdown,
    DropdownDivider,
    DropdownHeader,
    DropdownItem,
    Footer,
    FooterIcon,
    FooterBrand,
    FooterCopyright,
    FooterLink,
    FooterLinkGroup,
    TextInput,
    Label,
    FileInput,
    Select,
    Checkbox,
    Radio,
    ToggleSwitch,
    ListGroup,
    ListGroupItem,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    Navbar,
    NavbarBrand,
    NavbarCollapse,
    NavbarLink,
    NavbarToggle,
    Pagination,
    Progress,
    Sidebar,
    SidebarCTA,
    SidebarCollapse,
    SidebarItem,
    SidebarItemGroup,
    SidebarItemWrapper,
    SidebarLogo,
    SidebarItems,
    Spinner,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeadCell,
    TableRow,
    Toast,
    ToastToggle,
    Rating,
    RatingAdvanced,
    RatingStar,
    Accordion,
    AccordionItem,
  } from '$lib';

  import {
    InformationCircleSolid,
    EyeSolid,
    CheckSolid,
    ClockSolid,
    HomeSolid,
    ShoppingCartSolid,
    ArrowRightOutline,
    XSolid,
    ExclamationOutline,
    ChartPieSolid,
    ViewBoardsSolid,
    InboxInSolid,
    UserSolid,
    ArrowSmRightSolid,
    TableSolid,
    InboxSolid,
    ShoppingBagOutline,
    CheckOutline,
    XOutline,
    PlayOutline,
    PaperAirplaneOutline,
    LockOpenSolid,
    LockOpenOutline,
  } from 'svelte-heros';

  const onClick = (g) => {
    alert(g.detail);
  };

  let modalOpen1 = false;
  let modalOpen2 = false;
  let navOpen1 = false;
  let navOpen2 = false;
  let collapse = false;
</script>

<div class="p-4 max-w-5xl mx-auto space-y-4">
  <Alert color="blue">
    <span>
      <span class="font-medium"> Info alert! </span>
      Change a few things up and try submitting again.
    </span>
  </Alert>

  <Alert color="green" rounded={false} withBorderAccent={true} onDismiss={() => {}} icon={InformationCircleSolid}>
    <h3 class="text-lg font-medium text-green-700 dark:text-green-800">This is a info alert</h3>
    <div slot="extra">
      <div class="mt-2 mb-4 text-sm text-green-700 dark:text-green-800">
        More info about this info alert goes here. This example text is going to run a bit longer so that you can see
        how spacing within an alert works with this kind of content.
      </div>
      <div class="flex">
        <button
          type="button"
          class="mr-2 inline-flex items-center rounded-lg bg-green-700 px-3 py-1.5 text-center text-xs font-medium text-white hover:bg-green-800 focus:ring-4 focus:ring-green-300 dark:bg-green-800 dark:hover:bg-green-900"
        >
          <EyeSolid class="-ml-0.5 mr-2 h-4 w-4" />View more
        </button>
        <button
          type="button"
          class="rounded-lg border border-green-700 bg-transparent px-3 py-1.5 text-center text-xs font-medium text-green-700 hover:bg-green-800 hover:text-white focus:ring-4 focus:ring-green-300 dark:border-green-800 dark:text-green-800 dark:hover:text-white"
        >
          Dismiss
        </button>
      </div>
    </div>
  </Alert>

  <div class="flex flex-wrap gap-2">
    <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded={true} />
    <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" />
  </div>

  <div class="flex flex-wrap gap-2">
    <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded={true} bordered={true} />
    <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" bordered={true} />
  </div>

  <div class="flex flex-wrap gap-2">
    <Avatar />
    <Avatar rounded={true} />
  </div>

  <div class="flex flex-wrap gap-2">
    <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" status="online" />
    <Avatar
      img="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
      rounded={true}
      status="busy"
      statusPosition="top-left"
    />
    <Avatar
      img="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
      status="offline"
      statusPosition="bottom-right"
    />
    <Avatar
      img="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
      rounded={true}
      status="away"
      statusPosition="bottom-left"
    />
  </div>

  <div>
    <AvatarGroup>
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-1.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-2.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-3.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-4.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded={true} stacked={true} />
    </AvatarGroup>
    <AvatarGroup>
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-1.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-2.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-3.jpg" rounded={true} stacked={true} />
      <Avatar img="https://flowbite.com/docs/images/people/profile-picture-4.jpg" rounded={true} stacked={true} />
      <AvatarGroupCounter total={99} href="#" />
    </AvatarGroup>
  </div>

  <div class="flex flex-wrap gap-2">
    <Badge icon={CheckSolid}>2 minutes ago</Badge>
    <Badge color="gray" icon={ClockSolid}>3 days ago</Badge>
  </div>

  <div>
    <Breadcrumb aria-label="Default breadcrumb example">
      <BreadcrumbItem href="#" icon={HomeSolid}>Home</BreadcrumbItem>
      <BreadcrumbItem href="#">Projects</BreadcrumbItem>
      <BreadcrumbItem>Flowbite Svelte</BreadcrumbItem>
    </Breadcrumb>
  </div>

  <div class="flex flex-wrap gap-2">
    <Button>Default</Button>
    <Button color="alternative">Alternative</Button>
    <Button color="dark">Dark</Button>
    <Button color="light">Light</Button>
    <Button color="green">Green</Button>
    <Button color="red">Red</Button>
    <Button color="yellow">Yellow</Button>
    <Button color="purple">Purple</Button>
  </div>

  <div class="flex flex-wrap gap-2">
    <Button pill={true}>Default</Button>
    <Button color="alternative" pill={true}>Alternative</Button>
    <Button color="dark" pill={true}>Dark</Button>
    <Button color="light" pill={true}>Light</Button>
    <Button color="green" pill={true}>Green</Button>
    <Button color="red" pill={true}>Red</Button>
    <Button color="yellow" pill={true}>Yellow</Button>
    <Button color="purple" pill={true}>Purple</Button>
  </div>

  <div class="flex flex-wrap gap-2">
    <Button gradientMonochrome="blue">Blue</Button>
    <Button gradientMonochrome="green">Green</Button>
    <Button gradientMonochrome="cyan">Cyan</Button>
    <Button gradientMonochrome="teal">Teal</Button>
    <Button gradientMonochrome="lime">Lime</Button>
    <Button gradientMonochrome="red">Red</Button>
    <Button gradientMonochrome="pink">Pink</Button>
    <Button gradientMonochrome="purple">Purple</Button>
  </div>

  <div class="flex flex-wrap items-center gap-2">
    <Button outline={true} gradientDuoTone="purpleToBlue">Purple to Blue</Button>
    <Button outline={true} gradientDuoTone="cyanToBlue">Cyan to Blue</Button>
    <Button outline={true} gradientDuoTone="greenToBlue">Green to Blue</Button>
    <Button outline={true} gradientDuoTone="purpleToPink">Purple to Pink</Button>
    <Button outline={true} gradientDuoTone="pinkToOrange">Pink to Orange</Button>
    <Button outline={true} gradientDuoTone="tealToLime">Teal to Lime</Button>
    <Button outline={true} gradientDuoTone="redToYellow">Red to Yellow</Button>
  </div>

  <div class="flex flex-wrap items-center gap-2">
    <Button size="xs">Extra small</Button>
    <Button size="sm">Small</Button>
    <Button size="md">Base</Button>
    <Button size="lg">Large</Button>
    <Button size="xl">Extra large</Button>
  </div>

  <div class="flex flex-wrap items-center gap-2">
    <Button>
      <ShoppingCartSolid class="mr-2 h-5 w-5" />
      Buy now
    </Button>
    <Button>
      Choose plan
      <ArrowRightOutline class="ml-2 h-5 w-5" />
    </Button>
  </div>

  <Button label="2">Messages</Button>

  <div class="flex flex-wrap items-center gap-2">
    <Button icon={ArrowRightOutline} />
    <Button icon={ArrowRightOutline} pill={true} />
    <Button icon={ArrowRightOutline} outline={true} />
    <Button icon={ArrowRightOutline} pill={true} outline={true} />
    <Button disabled={true}>Disabled button</Button>
  </div>

  <Card
    class="max-w-sm"
    imgAlt="Meaningful alt text for an image that is not purely decorative"
    imgSrc="https://flowbite.com/docs/images/blog/image-1.jpg"
  >
    <h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      Noteworthy technology acquisitions 2021
    </h5>
    <p class="font-normal text-gray-700 dark:text-gray-400">
      Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
    </p>
  </Card>

  <Card class="max-w-sm" imgSrc="https://flowbite.com/docs/images/blog/image-4.jpg" horizontal={true}>
    <h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      Noteworthy technology acquisitions 2021
    </h5>
    <p class="font-normal text-gray-700 dark:text-gray-400">
      Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
    </p>
  </Card>

  <div class="flex gap-2">
    <Tooltip content="Tooltip content" style="light">
      <Button>Light tooltip</Button>
    </Tooltip>
    <Tooltip content="Tooltip content" style="dark">
      <Button>Dark tooltip</Button>
    </Tooltip>
  </div>

  <div class="flex gap-2">
    <Tooltip content="Tooltip content" placement="top">
      <Button>Tooltip top</Button>
    </Tooltip>
    <Tooltip content="Tooltip content" placement="right">
      <Button>Tooltip right</Button>
    </Tooltip>
    <Tooltip content="Tooltip content" placement="bottom">
      <Button>Tooltip bottom</Button>
    </Tooltip>
    <Tooltip content="Tooltip content" placement="left">
      <Button>Tooltip left</Button>
    </Tooltip>
  </div>

  <div class="flex gap-2">
    <Tooltip content="Tooltip content" trigger="hover">
      <Button>Tooltip hover</Button>
    </Tooltip>
    <Tooltip content="Tooltip content" trigger="click">
      <Button>Tooltip click</Button>
    </Tooltip>
  </div>

  <div class="flex">
    <Tooltip content="Tooltip content" arrow={false}>
      <Button>Default tooltip</Button>
    </Tooltip>
  </div>

  <div class="flex gap-4">
    <Dropdown label="Dropdown button">
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem>Separated link</DropdownItem>
    </Dropdown>
    <Dropdown label="Dropdown" inline={true}>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
    <Dropdown label="Dropdown">
      <DropdownItem data={1} on:click={onClick}>Dashboard</DropdownItem>
      <DropdownItem data={2} on:click={onClick}>Settings</DropdownItem>
      <DropdownItem data={3} on:click={onClick}>Earnings</DropdownItem>
      <DropdownItem data={4} on:click={onClick}>Sign out</DropdownItem>
    </Dropdown>
  </div>

  <Footer>
    <FooterCopyright href="#" by="Flowbite™" year={2022} />
    <FooterLinkGroup class="mt-3 flex-wrap items-center text-sm sm:mt-0">
      <FooterLink href="#">About</FooterLink>
      <FooterLink href="#">Privacy Policy</FooterLink>
      <FooterLink href="#">Licensing</FooterLink>
      <FooterLink href="#">Contact</FooterLink>
    </FooterLinkGroup>
  </Footer>

  <Footer class="flex flex-col">
    <div class="grid w-full justify-between sm:flex sm:justify-between md:flex md:grid-cols-1">
      <div>
        <FooterBrand
          href="https://flowbite.com"
          src="https://flowbite.com/docs/images/logo.svg"
          alt="Flowbite Logo"
          name="Flowbite"
          class="m-6"
        />
      </div>
      <div class="grid grid-cols-2 gap-8 sm:mt-4 sm:grid-cols-3 sm:gap-6">
        <div>
          <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">About</h2>
          <FooterLinkGroup class="flex-col">
            <FooterLink class="mb-4" href="#">Flowbite</FooterLink>
            <FooterLink class="mb-4" href="#">Tailwind CSS</FooterLink>
          </FooterLinkGroup>
        </div>
        <div>
          <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Follow us</h2>
          <FooterLinkGroup class="flex-col">
            <FooterLink class="mb-4" href="#">Gihub</FooterLink>
            <FooterLink class="mb-4" href="#">Discord</FooterLink>
          </FooterLinkGroup>
        </div>
        <div>
          <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Legal</h2>
          <FooterLinkGroup class="flex-col">
            <FooterLink class="mb-4" href="#">Privacy Policy</FooterLink>
            <FooterLink class="mb-4" href="#">Terms & Conditions</FooterLink>
          </FooterLinkGroup>
        </div>
      </div>
    </div>
    <hr class="my-6 w-full border-gray-200 p-1 dark:border-gray-700 sm:mx-auto lg:my-8" />
    <div class="w-full sm:flex sm:items-center sm:justify-between">
      <FooterCopyright href="#" by="Flowbite™" year={2022} />
      <div class="mt-4 flex space-x-6 sm:mt-0 sm:justify-center">
        <FooterIcon href="#" class="text-gray-400 hover:text-gray-900" icon={CheckSolid} />
        <FooterIcon href="#" class="text-gray-400 hover:text-gray-900" icon={CheckSolid} />
        <FooterIcon href="#" class="text-gray-400 hover:text-gray-900" icon={CheckSolid} />
        <FooterIcon href="#" class="text-gray-400 hover:text-gray-900" icon={CheckSolid} />
        <FooterIcon href="#" class="text-gray-400 hover:text-gray-900" icon={CheckSolid} />
      </div>
    </div>
  </Footer>

  <div>
    <div>
      <Label class="mb-2 block" for="email">Your email</Label>
      <TextInput
        id="email"
        type="email"
        placeholder="name@flowbite.com"
        required={true}
        helperText={"We'll never share your details."}
      />
    </div>
    <div>
      <Label class="mb-2 block" for="dsa">Your email</Label>
      <TextInput id="dsa" type="email" placeholder="name@flowbite.com" required={true}>
        <div slot="helper">
          We'll never share your details. Read our <a
            href="/forms"
            class="font-medium text-blue-600 hover:underline dark:text-blue-500">Privacy Policy</a
          >.
        </div>
      </TextInput>
    </div>
  </div>

  <div id="fileUpload">
    <Label class="mb-2 block" for="file">Upload file</Label>
    <FileInput id="file" helperText="A profile picture is useful to confirm your are logged into your account" />
  </div>

  <div>
    <div id="select">
      <Label class="mb-2 block" for="countries">Select your country</Label>
      <Select id="countries" required={true}>
        <option selected> United States </option>
        <option> Canada </option>
        <option> France </option>
        <option> Germany </option>
      </Select>
    </div>
  </div>

  <div class="flex flex-col gap-4" id="checkbox">
    <div class="flex items-center gap-2">
      <Checkbox id="accept" defaultChecked={true} />
      <Label for="accept">
        I agree to the{' '}
        <a href="/forms" class="text-blue-600 hover:underline dark:text-blue-500"> terms and conditions </a>
      </Label>
    </div>
    <div class="flex items-center gap-2">
      <Checkbox id="promotion" />
      <Label for="promotion">I want to get promotional offers</Label>
    </div>
    <div class="flex items-center gap-2">
      <Checkbox id="age" />
      <Label for="age">I am 18 years or older</Label>
    </div>
    <div class="flex gap-2">
      <div class="flex h-5 items-center">
        <Checkbox id="shipping" />
      </div>
      <div class="flex flex-col">
        <Label for="shipping">Free shipping via Flowbite</Label>
        <div class="text-gray-500 dark:text-gray-300">
          <span class="text-xs font-normal">
            For orders shipped from Flowbite from{' '}
            <span class="font-medium"> € 25 </span>
            {' '}in books or{' '}
            <span> € 29 </span>
            {' '}on other categories
          </span>
        </div>
      </div>
    </div>
    <div class="flex items-center gap-2">
      <Checkbox id="disabled" disabled={true} />
      <Label for="disabled" class="opacity-50">Eligible for international shipping (disabled)</Label>
    </div>
  </div>

  <div>
    <fieldset class="flex flex-col gap-4" id="radio">
      <div class="flex items-center gap-2">
        <Radio id="united-state" name="countries" value="USA" defaultChecked={true} />
        <Label for="united-state">United States</Label>
      </div>
      <div class="flex items-center gap-2">
        <Radio id="germany" name="countries" value="Germany" />
        <Label for="germany">Germany</Label>
      </div>
      <div class="flex items-center gap-2">
        <Radio id="spain" name="countries" value="Spain" />
        <Label for="spain">Spain</Label>
      </div>
      <div class="flex items-center gap-2">
        <Radio id="uk" name="countries" value="United Kingdom" />
        <Label for="uk">United Kingdom</Label>
      </div>
      <div class="flex items-center gap-2">
        <Radio id="china" name="countries" value="China" disabled={true} />
        <Label class="opacity-50" for="china">China (disabled)</Label>
      </div>
    </fieldset>
  </div>

  <div class="flex flex-col gap-4" id="toggle">
    <ToggleSwitch label="Toggle me" />
    <ToggleSwitch label="Toggle me (checked)" checked={true} />
    <ToggleSwitch label="Toggle me (disabled)" disabled={true} />
  </div>

  <div>
    <ListGroup class="w-48">
      <ListGroupItem active={true} icon={HomeSolid}>Profile</ListGroupItem>
      <ListGroupItem icon={CheckSolid}>Settings</ListGroupItem>
      <ListGroupItem icon={XSolid}>Messages</ListGroupItem>
      <ListGroupItem icon={InformationCircleSolid}>Download</ListGroupItem>
    </ListGroup>
  </div>

  <div>
    <Button on:click={() => (modalOpen1 = true)}>Toggle modal</Button>
    <Modal bind:open={modalOpen1} on:close={() => alert('closed')}>
      <ModalHeader>Terms of Service</ModalHeader>
      <ModalBody class="space-y-6">
        <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
          With less than a month to go before the European Union enacts new consumer privacy laws for its citizens,
          companies around the world are updating their terms of service agreements to comply.
        </p>
        <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
          The European Union's General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to
          ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as
          possible of high-risk data breaches that could personally affect them.
        </p>
      </ModalBody>
      <ModalFooter>
        <Button on:click={() => (modalOpen1 = false)}>I accept</Button>
        <Button color="alternative" on:click={() => (modalOpen1 = false)}>Decline</Button>
      </ModalFooter>
    </Modal>
  </div>

  <div>
    <Button on:click={() => (modalOpen2 = true)}>Toggle modal</Button>
    <Modal bind:open={modalOpen2} size="md" popup={true}>
      <ModalHeader />
      <ModalBody class="text-center">
        <ExclamationOutline class="mx-auto mb-4 h-14 w-14 text-gray-400 dark:text-gray-200" />
        <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
          Are you sure you want to delete this product?
        </h3>
        <div class="flex justify-center gap-4">
          <Button color="red" {onClick}>Yes, I'm sure</Button>
          <Button color="alternative" {onClick}>No, cancel</Button>
        </div>
      </ModalBody>
    </Modal>
  </div>

  <div>
    <Navbar fluid={true} rounded={true}>
      <NavbarBrand href="https://flowbite.com/">
        <img src="https://flowbite.com/docs/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"> Flowbite </span>
      </NavbarBrand>
      <div class="flex md:order-2">
        <Button>Get started</Button>
        <NavbarToggle bind:open={navOpen1} />
      </div>
      <NavbarCollapse bind:open={navOpen1}>
        <NavbarLink href="/navbars" active={true}>Home</NavbarLink>
        <NavbarLink href="/navbars">About</NavbarLink>
        <NavbarLink href="/navbars">Services</NavbarLink>
        <NavbarLink href="/navbars">Pricing</NavbarLink>
        <NavbarLink href="/navbars">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  </div>

  <div>
    <Navbar fluid={true} rounded={true}>
      <NavbarBrand href="https://flowbite.com/">
        <img src="https://flowbite.com/docs/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"> Flowbite </span>
      </NavbarBrand>
      <div class="flex md:order-2">
        <Dropdown arrowIcon={false} inline={true}>
          <Avatar
            slot="label"
            alt="User settings"
            img="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
            rounded={true}
          />
          <DropdownHeader>
            <span class="block text-sm"> Bonnie Green </span>
            <span class="block truncate text-sm font-medium"> name@flowbite.com </span>
          </DropdownHeader>
          <DropdownItem>Dashboard</DropdownItem>
          <DropdownItem>Settings</DropdownItem>
          <DropdownItem>Earnings</DropdownItem>
          <DropdownDivider />
          <DropdownItem>Sign out</DropdownItem>
        </Dropdown>
        <NavbarToggle bind:open={navOpen2} />
      </div>
      <NavbarCollapse bind:open={navOpen2}>
        <NavbarLink href="/navbars" active={true}>Home</NavbarLink>
        <NavbarLink href="/navbars">About</NavbarLink>
        <NavbarLink href="/navbars">Services</NavbarLink>
        <NavbarLink href="/navbars">Pricing</NavbarLink>
        <NavbarLink href="/navbars">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  </div>

  <Pagination currentPage={5} totalPages={100} />

  <Pagination currentPage={5} showIcons={true} totalPages={100} />

  <div class="flex items-center justify-center text-center">
    <Pagination currentPage={5} layout="table" totalPages={1000} />
  </div>

  <div class="flex flex-col gap-2">
    <div class="text-base font-medium dark:text-white">Small</div>
    <Progress progress={45} size="sm" color="dark" />
    <div class="text-base font-medium dark:text-white">Default</div>
    <Progress progress={45} size="md" color="dark" />
    <div class="text-lg font-medium dark:text-white">Large</div>
    <Progress progress={45} size="lg" color="dark" />
    <div class="text-lg font-medium dark:text-white">Extra Large</div>
    <Progress progress={45} size="xl" color="dark" />
  </div>

  <div class="flex flex-col gap-2">
    <div class="text-base font-medium">Dark</div>
    <Progress progress={45} color="dark" />
    <div class="text-base font-medium text-blue-700">Blue</div>
    <Progress progress={45} color="blue" />
    <div class="text-base font-medium text-red-700">Red</div>
    <Progress progress={45} color="red" />
    <div class="text-base font-medium text-green-700">Green</div>
    <Progress progress={45} color="green" />
    <div class="text-base font-medium text-yellow-700">Yellow</div>
    <Progress progress={45} color="yellow" />
    <div class="text-base font-medium text-indigo-700">Indigo</div>
    <Progress progress={45} color="indigo" />
    <div class="text-base font-medium text-purple-700">Purple</div>
    <Progress progress={45} color="purple" />
  </div>
  <Progress progress={50} label="Flowbite" size="lg" />
  <Progress progress={45} label="Flowbite" labelPosition="outside" labelProgress={true} />

  <div>
    <Checkbox bind:checked={collapse} />
    <Sidebar class="!bg-gray-50" collapsed={collapse}>
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={ChartPieSolid}>Dashboard</SidebarItem>
          <SidebarItem href="#" icon={ViewBoardsSolid} label="Pro" labelColor="gray">Kanban</SidebarItem>
          <SidebarItem href="#" icon={InboxInSolid} label="3">Inbox</SidebarItem>
          <SidebarItem href="#" icon={UserSolid}>Users</SidebarItem>
          <SidebarItem href="#" icon={ShoppingCartSolid}>Products</SidebarItem>
          <SidebarItem href="#" icon={ArrowSmRightSolid}>Sign In</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Sign Up</SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  </div>

  <div>
    <Sidebar class="!bg-gray-50" collapsed={false}>
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={ChartPieSolid}>Dashboard</SidebarItem>
          <SidebarCollapse icon={UserSolid} label="E-commerce">
            <SidebarItem href="#">Products</SidebarItem>
          </SidebarCollapse>
          <SidebarItem href="#" icon={InboxSolid}>Inbox</SidebarItem>
          <SidebarItem href="#" icon={UserSolid}>Users</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Products</SidebarItem>
          <SidebarItem href="#" icon={ArrowSmRightSolid}>Sign In</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Sign Up</SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  </div>

  <div>
    <Sidebar class="!bg-gray-50" collapsed={false}>
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={ChartPieSolid}>Dashboard</SidebarItem>
          <SidebarItem href="#" icon={ViewBoardsSolid}>Kanban</SidebarItem>
          <SidebarItem href="#" icon={InboxSolid}>Inbox</SidebarItem>
          <SidebarItem href="#" icon={UserSolid}>Users</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Products</SidebarItem>
          <SidebarItem href="#" icon={ArrowSmRightSolid}>Sign In</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Sign Up</SidebarItem>
        </SidebarItemGroup>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={ChartPieSolid}>Upgrade to Pro</SidebarItem>
          <SidebarItem href="#" icon={ViewBoardsSolid}>Documentation</SidebarItem>
          <SidebarItem href="#" icon={UserSolid}>Help</SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  </div>

  <div>
    <Sidebar class="!bg-gray-50" collapsed={false}>
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={ChartPieSolid}>Dashboard</SidebarItem>
          <SidebarItem href="#" icon={ViewBoardsSolid}>Kanban</SidebarItem>
          <SidebarItem href="#" icon={InboxSolid}>Inbox</SidebarItem>
          <SidebarItem href="#" icon={UserSolid}>Users</SidebarItem>
          <SidebarItem href="#" icon={ShoppingBagOutline}>Products</SidebarItem>
          <SidebarItem href="#" icon={ArrowSmRightSolid}>Sign In</SidebarItem>
          <SidebarItem href="#" icon={TableSolid}>Sign Up</SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
      <SidebarCTA>
        <div class="mb-3 flex items-center">
          <Badge color="yellow">Beta</Badge>
        </div>
        <p class="mb-3 text-sm text-blue-900 dark:text-blue-400">
          Preview the new Flowbite dashboard navigation! You can turn the new navigation off for a limited time in your
          profile.
        </p>
        <a
          class="text-sm text-blue-900 underline hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300"
          href="#"
        >
          Turn new navigation off
        </a>
      </SidebarCTA>
    </Sidebar>
  </div>

  <div>
    <div class="flex flex-wrap items-center gap-2">
      <Spinner aria-label="Extra small spinner example" size="xs" />
      <Spinner aria-label="Small spinner example" size="sm" />
      <Spinner aria-label="Medium sized spinner example" size="md" />
      <Spinner aria-label="Large spinner example" size="lg" />
      <Spinner aria-label="Extra large spinner example" size="xl" />
    </div>
  </div>

  <div class="flex flex-col gap-2">
    <div class="text-left">
      <Spinner aria-label="Left-aligned spinner example" />
    </div>
    <div class="text-center">
      <Spinner aria-label="Center-aligned spinner example" />
    </div>
    <div class="text-right">
      <Spinner aria-label="Right-aligned spinner example" />
    </div>
  </div>

  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell>Product name</TableHeadCell>
      <TableHeadCell>Color</TableHeadCell>
      <TableHeadCell>Category</TableHeadCell>
      <TableHeadCell>Price</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only"> Edit </span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Apple MacBook Pro 17"</TableCell>
        <TableCell>Sliver</TableCell>
        <TableCell>Laptop</TableCell>
        <TableCell>$2999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Microsoft Surface Pro</TableCell>
        <TableCell>White</TableCell>
        <TableCell>Laptop PC</TableCell>
        <TableCell>$1999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
        <TableCell>Black</TableCell>
        <TableCell>Accessories</TableCell>
        <TableCell>$99</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>

  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell class="!p-4">
        <Checkbox />
      </TableHeadCell>
      <TableHeadCell>Product name</TableHeadCell>
      <TableHeadCell>Color</TableHeadCell>
      <TableHeadCell>Category</TableHeadCell>
      <TableHeadCell>Price</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only"> Edit </span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="!p-4">
          <Checkbox />
        </TableCell>
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Apple MacBook Pro 17"</TableCell>
        <TableCell>Sliver</TableCell>
        <TableCell>Laptop</TableCell>
        <TableCell>$2999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="!p-4">
          <Checkbox />
        </TableCell>
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Microsoft Surface Pro</TableCell>
        <TableCell>White</TableCell>
        <TableCell>Laptop PC</TableCell>
        <TableCell>$1999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="!p-4">
          <Checkbox />
        </TableCell>
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
        <TableCell>Black</TableCell>
        <TableCell>Accessories</TableCell>
        <TableCell>$99</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>

  <Table striped={true}>
    <TableHead>
      <TableHeadCell>Product name</TableHeadCell>
      <TableHeadCell>Color</TableHeadCell>
      <TableHeadCell>Category</TableHeadCell>
      <TableHeadCell>Price</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only"> Edit </span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Apple MacBook Pro 17"</TableCell>
        <TableCell>Sliver</TableCell>
        <TableCell>Laptop</TableCell>
        <TableCell>$2999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Microsoft Surface Pro</TableCell>
        <TableCell>White</TableCell>
        <TableCell>Laptop PC</TableCell>
        <TableCell>$1999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
        <TableCell>Black</TableCell>
        <TableCell>Accessories</TableCell>
        <TableCell>$99</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Google Pixel Phone</TableCell>
        <TableCell>Gray</TableCell>
        <TableCell>Phone</TableCell>
        <TableCell>$799</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
      <TableRow class="bg-white dark:border-gray-700 dark:bg-gray-800">
        <TableCell class="whitespace-nowrap font-medium text-gray-900 dark:text-white">Apple Watch 5</TableCell>
        <TableCell>Red</TableCell>
        <TableCell>Wearables</TableCell>
        <TableCell>$999</TableCell>
        <TableCell>
          <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500"> Edit </a>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>

  <div>
    <div class="flex flex-col gap-4">
      <Toast>
        <div
          class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-green-100 text-green-500 dark:bg-green-800 dark:text-green-200"
        >
          <CheckOutline class="h-5 w-5" />
        </div>
        <div class="ml-3 text-sm font-normal">Item moved successfully.</div>
        <ToastToggle />
      </Toast>
      <Toast>
        <div
          class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-red-100 text-red-500 dark:bg-red-800 dark:text-red-200"
        >
          <XOutline class="h-5 w-5" />
        </div>
        <div class="ml-3 text-sm font-normal">Item has been deleted.</div>
        <ToastToggle />
      </Toast>
      <Toast>
        <div
          class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-orange-100 text-orange-500 dark:bg-orange-700 dark:text-orange-200"
        >
          <ExclamationOutline class="h-5 w-5" />
        </div>
        <div class="ml-3 text-sm font-normal">Improve password difficulty.</div>
        <ToastToggle />
      </Toast>
    </div>
  </div>

  <div class="space-y-4">
    <Toast class="space-x-4 divide-x divide-gray-200 dark:divide-gray-700">
      <PaperAirplaneOutline class="h-5 w-5 text-blue-600 dark:text-blue-500" />
      <div class="pl-4 text-sm font-normal">Message sent successfully.</div>
    </Toast>

    <Toast>
      <div class="text-sm font-normal">Conversation archived.</div>
      <div class="ml-auto flex items-center space-x-2">
        <a
          class="rounded-lg p-1.5 text-sm font-medium text-blue-600 hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-700"
          href="/toast"
        >
          Undo
        </a>
        <ToastToggle />
      </div>
    </Toast>
  </div>

  <div>
    <Toast class="!items-start">
      <div
        class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 text-blue-500 dark:bg-blue-900 dark:text-blue-300"
      >
        <LockOpenOutline class="h-5 w-5" />
      </div>
      <div class="ml-3 text-sm font-normal">
        <span class="mb-1 text-sm font-semibold text-gray-900 dark:text-white"> Update available </span>
        <div class="mb-2 text-sm font-normal">A new software version is available for download.</div>
        <div class="flex gap-2">
          <Button class="!w-full" size="xs">Update</Button>
          <Button class="!w-full" color="light" size="xs">Not now</Button>
        </div>
      </div>
      <ToastToggle />
    </Toast>
  </div>

  <div class="flex flex-col gap-4">
    <Rating>
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar filled={false} />
      <p class="ml-2 text-sm font-medium text-gray-500 dark:text-gray-400">4.95 out of 5</p>
    </Rating>
    <p class="text-sm font-medium text-gray-500 dark:text-gray-400">1,745 global ratings</p>
    <RatingAdvanced percentFilled={70}>5 star</RatingAdvanced>
    <RatingAdvanced percentFilled={17}>4 star</RatingAdvanced>
    <RatingAdvanced percentFilled={8}>3 star</RatingAdvanced>
    <RatingAdvanced percentFilled={4}>2 star</RatingAdvanced>
    <RatingAdvanced percentFilled={1}>1 star</RatingAdvanced>
  </div>

  <Accordion>
    <AccordionItem open={true}>
      <div slot="title">What is Flowbite?</div>
      <p class="mb-2 text-gray-500 dark:text-gray-400">
        Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons,
        dropdowns, modals, navbars, and more.
      </p>
      <p class="text-gray-500 dark:text-gray-400">
        Check out this guide to learn how to{' '}
        <a
          href="https://flowbite.com/docs/getting-started/introduction/"
          class="text-blue-600 hover:underline dark:text-blue-500"
        >
          get started
        </a>
        {' '}and start developing websites even faster with components on top of Tailwind CSS.
      </p>
    </AccordionItem>
    <AccordionItem>
      <div slot="title">Is there a Figma file available?</div>
      <p class="mb-2 text-gray-500 dark:text-gray-400">
        Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has
        a design equivalent in our Figma file.
      </p>
      <p class="text-gray-500 dark:text-gray-400">
        Check out the{' '}
        <a href="https://flowbite.com/figma/" class="text-blue-600 hover:underline dark:text-blue-500">
          Figma design system
        </a>
        {' '}based on the utility classes from Tailwind CSS and components from Flowbite.
      </p>
    </AccordionItem>
    <AccordionItem>
      <div slot="title">What are the differences between Flowbite and Tailwind UI?</div>
      <p class="mb-2 text-gray-500 dark:text-gray-400">
        The main difference is that the core components from Flowbite are open source under the MIT license, whereas
        Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components,
        whereas Tailwind UI offers sections of pages.
      </p>
      <p class="mb-2 text-gray-500 dark:text-gray-400">
        However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical
        reason stopping you from using the best of two worlds.
      </p>
      <p class="mb-2 text-gray-500 dark:text-gray-400">Learn more about these technologies:</p>
      <ul class="list-disc pl-5 text-gray-500 dark:text-gray-400">
        <li>
          <a href="https://flowbite.com/pro/" class="text-blue-600 hover:underline dark:text-blue-500">
            Flowbite Pro
          </a>
        </li>
        <li>
          <a href="https://tailwindui.com/" rel="nofollow" class="text-blue-600 hover:underline dark:text-blue-500">
            Tailwind UI
          </a>
        </li>
      </ul>
    </AccordionItem>
  </Accordion>
</div>
