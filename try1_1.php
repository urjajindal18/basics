<?php

echo "<input type=\"text\" name=\"name\" >";   //to diable comas add backslash before it

echo "  <input type='text' name='name' >";   // or we cn use different comas for different places

echo '  <input type="text" name="name" >'; // this is also correct and  more prefered as well

$text=' my name is urja';
?>
<input type="text" value="<?php echo $text; ?>">      //here we have embedded php into html statement