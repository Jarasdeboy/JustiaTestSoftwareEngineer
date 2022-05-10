## Question 9: Building a Car

When putting together a wheel for a car, one picks a tire that is compatible with a rim. 

```php
<?php 

class Wheel
{
    private $tire;
    private $rim;

    public function __construct ($width, $diameter, $section_width, $aspect_ratio)
    {
        $this->tire = new Tire($section_width, $diameter, $aspect_ratio);
        $this->rim = new Rim($width, $diameter);
    }

    public function getTire() 
    {
        return $this->tire;
    }

    public function getRim()
    {
        return $this->rim;
    }
}

class Tire
{
    private $section_width;
    private $diameter;
    private $aspect_ratio;

    public function __construct($section_width, $diameter, $aspect_ratio) {/* ... */}
    
    // Getters & Setters
}

class Rim
{
        private $rim_width;
        private $diameter;

        public function __construct($rim_width, $diameter) {/* ... */}

        // Getters & Setters
}

```

The above code violates the dependency inversion principle which causes some tight coupling of classes. Use dependency injection to recode the Wheel, Tire, and Rim classes. Please rewrite this in any language.

### Answer
  


