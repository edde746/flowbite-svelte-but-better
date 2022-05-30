<script>
  import {
    Timeline,
    TimelineBody,
    TimelineContent,
    TimelineItem,
    TimelinePoint,
    TimelineTime,
    TimelineTitle,
    Button,
  } from '$lib';

  import Card from '$lib/Card/Card.svelte';
  import { HiArrowRightSolid, HiCalendarSolid } from 'svelte-icons/hi';
  import { HighlightSvelte } from 'svelte-highlight';
</script>

<div class="mx-auto flex max-w-4xl flex-col gap-8 dark:text-white">
  <div class="flex flex-col gap-2">
    <span class="text-2xl font-bold">Default timeline</span>
    <Card>
      <Timeline>
        <TimelineItem>
          <TimelinePoint />
          <TimelineContent>
            <TimelineTime>February 2022</TimelineTime>
            <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
            <TimelineBody>
              Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
              E-commerce & Marketing pages.
            </TimelineBody>
            <Button color="alternative">
              Learn More
              <HiArrowRightSolid class="ml-2 h-4 w-4" />
            </Button>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint />
          <TimelineContent>
            <TimelineTime>March 2022</TimelineTime>
            <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
            <TimelineBody>
              All of the pages and components are first designed in Figma and we keep a parity between the two versions
              even as we update the project.
            </TimelineBody>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint />
          <TimelineContent>
            <TimelineTime>April 2022</TimelineTime>
            <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
            <TimelineBody>
              Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
            </TimelineBody>
          </TimelineContent>
        </TimelineItem>
      </Timeline>
      <HighlightSvelte
        code={`<Timeline>
  <TimelineItem>
    <TimelinePoint />
    <TimelineContent>
      <TimelineTime>February 2022</TimelineTime>
      <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
      <TimelineBody>
        Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
        E-commerce & Marketing pages.
      </TimelineBody>
      <Button color="alternative">
        Learn More
        <HiArrowRightSolid class="ml-2 h-4 w-4" />
      </Button>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint />
    <TimelineContent>
      <TimelineTime>March 2022</TimelineTime>
      <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
      <TimelineBody>
        All of the pages and components are first designed in Figma and we keep a parity between the two versions
        even as we update the project.
      </TimelineBody>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint />
    <TimelineContent>
      <TimelineTime>April 2022</TimelineTime>
      <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
      <TimelineBody>
        Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
      </TimelineBody>
    </TimelineContent>
  </TimelineItem>
</Timeline>`}
      />
    </Card>
  </div>
  <div class="flex flex-col gap-2">
    <span class="text-2xl font-bold">Vertical timeline</span>
    <Card>
      <Timeline>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTime>February 2022</TimelineTime>
            <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
            <TimelineBody>
              Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
              E-commerce & Marketing pages.
            </TimelineBody>
            <Button color="alternative">
              Learn More
              <HiArrowRightSolid class="ml-2 h-4 w-4" />
            </Button>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTime>March 2022</TimelineTime>
            <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
            <TimelineBody>
              All of the pages and components are first designed in Figma and we keep a parity between the two versions
              even as we update the project.
            </TimelineBody>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTime>April 2022</TimelineTime>
            <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
            <TimelineBody>
              Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
            </TimelineBody>
          </TimelineContent>
        </TimelineItem>
      </Timeline>
      <HighlightSvelte
        code={`<Timeline>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTime>February 2022</TimelineTime>
      <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
      <TimelineBody>
        Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
        E-commerce & Marketing pages.
      </TimelineBody>
      <Button color="alternative">
        Learn More
        <HiArrowRightSolid class="ml-2 h-4 w-4" />
      </Button>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTime>March 2022</TimelineTime>
      <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
      <TimelineBody>
        All of the pages and components are first designed in Figma and we keep a parity between the two versions
        even as we update the project.
      </TimelineBody>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTime>April 2022</TimelineTime>
      <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
      <TimelineBody>
        Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
      </TimelineBody>
    </TimelineContent>
  </TimelineItem>
</Timeline>`}
      />
    </Card>
  </div>
  <div class="flex flex-col gap-2">
    <span class="text-2xl font-bold">Stepper timeline</span>
    <Card>
      <Timeline horizontal={true}>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTitle>Flowbite Library v1.0.0</TimelineTitle>
            <TimelineTime>Released on December 2, 2021</TimelineTime>
            <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTitle>Flowbite Library v1.2.0</TimelineTitle>
            <TimelineTime>Released on December 23, 2021</TimelineTime>
            <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelinePoint icon={HiCalendarSolid} />
          <TimelineContent>
            <TimelineTitle>Flowbite Library v1.3.0</TimelineTitle>
            <TimelineTime>Released on January 5, 2022</TimelineTime>
            <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
          </TimelineContent>
        </TimelineItem>
      </Timeline>
      <HighlightSvelte
        code={`<Timeline horizontal={true}>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTitle>Flowbite Library v1.0.0</TimelineTitle>
      <TimelineTime>Released on December 2, 2021</TimelineTime>
      <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTitle>Flowbite Library v1.2.0</TimelineTitle>
      <TimelineTime>Released on December 23, 2021</TimelineTime>
      <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
    </TimelineContent>
  </TimelineItem>
  <TimelineItem>
    <TimelinePoint icon={HiCalendarSolid} />
    <TimelineContent>
      <TimelineTitle>Flowbite Library v1.3.0</TimelineTitle>
      <TimelineTime>Released on January 5, 2022</TimelineTime>
      <TimelineBody>Get started with dozens of web components and interactive elements.</TimelineBody>
    </TimelineContent>
  </TimelineItem>
</Timeline>`}
      />
    </Card>
  </div>
</div>
