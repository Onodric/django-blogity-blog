/*
  Highlights by HTML5 UP
  html5up.net | @ajlkn
  Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

  skel.breakpoints({
    large: '(max-width: 1680px)',
    medium: '(max-width: 980px)',
    small: '(max-width: 736px)',
    xsmall: '(max-width: 480px)'
  });

  $(function() {

    var	$window = $(window),
      $body = $('body'),
      $html = $('html');

    // Disable animations/transitions until the page has loaded.
      $html.addClass('is-loading');

      $window.on('load', function() {
        window.setTimeout(function() {
          $html.removeClass('is-loading');
        }, 0);
        let parent = $('#id_draft').parent();
        $('label[for="id_draft"]').remove();
        $("<label>Is This a Draft?</label>").attr("for", "id_draft").appendTo(parent);
        $('.is_draft').attr('style', 'background: red; color: white');
      });

    // Touch mode.
      if (skel.vars.mobile) {

        var $wrapper;

        // Create wrapper.
          $body.wrapInner('<div id="wrapper" />');
          $wrapper = $('#wrapper');

          // Hack: iOS vh bug.
            if (skel.vars.os == 'ios')
              $wrapper
                .css('margin-top', -25)
                .css('padding-bottom', 25);

          // Pass scroll event to window.
            $wrapper.on('scroll', function() {
              $window.trigger('scroll');
            });

        // Scrolly.
          $window.on('load.hl_scrolly', function() {

            $('.scrolly').scrolly({
              speed: 1500,
              parent: $wrapper,
              pollOnce: true
            });

            $window.off('load.hl_scrolly');

          });

        // Enable touch mode.
          $html.addClass('is-touch');

      }
      else {

        // Scrolly.
          $('.scrolly').scrolly({
            speed: 1000
          });

      }

    // Fix: Placeholder polyfill.
      $('form').placeholder();

    // Prioritize "important" elements on medium.
      skel.on('+medium -medium', function() {
        $.prioritize(
          '.important\\28 medium\\29',
          skel.breakpoint('medium').active
        );
      });

    // Header.
      var $header = $('#header'),
        $headerTitle = $header.find('header'),
        $headerContainer = $header.find('.container'),
        $replacedText = $('#replace-text');

        let descriptors = [
          'n { earnest',
          'n { eager',
          ' { helpful',
          ' { smart',
          ' { curious',
          'n { all-around good',
          ' { great little',
          ' { talented',
          ' { fun',
          ' { funny',
          ' { serious',
          ' { focused',
          'n { extemporaneous',
          'n { anglophile',
          ' { supercool',
          'n { insufferable',
          ' { better',
          ' { good',
          'n { interested',
          'n { interesting'
      ];

      window.setInterval(function () {
        $replacedText.fadeOut(function () {
          $replacedText.text(descriptors[Math.floor(Math.random()*descriptors.length)]);
        });
        $replacedText.fadeIn();
      }, 1500);



      // Make title fixed.
        if (!skel.vars.mobile) {

          $window.on('load.hl_headerTitle', function() {

            skel.on('-medium !medium', function() {

              $headerTitle
                .css('position', 'fixed')
                .css('display', 'inline-block')
                .css('position', 'fixed')
                .css('height', 'auto')
                .css('top', '25%')
                .css('left', '25%')
                .css('width', '50%')
                .css('background', 'rgba(0,0,0,.6)')
                .css('box-shadow', '0 0 3em rgba(0,0,0,1)')
                .css('padding-top', '1em')
                .css('padding-bottom', '1em')

            });

            skel.on('+medium', function() {

              $headerTitle
                .css('position', 'fixed')
                .css('display', 'inline-block')
                .css('position', 'fixed')
                .css('height', 'auto')
                .css('top', '25%')
                .css('left', '25%')
                .css('width', '50%')
                .css('background', 'rgba(0,0,0,.6)')
                .css('box-shadow', '0 0 3em rgba(0,0,0,1)')
                .css('padding-top', '1em')
                .css('padding-bottom', '1em')

            });

            $window.off('load.hl_headerTitle');

          });

        }

      // Scrollex.
        skel.on('-small !small', function() {
          $header.scrollex({
            terminate: function() {

              $headerTitle.css('opacity', '');

            },
            scroll: function(progress) {

              // Fade out title as user scrolls down.
                if (progress > 0.5)
                  x = 1 - progress;
                else
                  x = progress;

                $headerTitle.css('opacity', Math.max(0, Math.min(1, x * 2)));

            }
          });
        });

        skel.on('+small', function() {

          $header.unscrollex();

        });

    // Main sections.
      $('.main').each(function() {

        var $this = $(this),
          $primaryImg = $this.find('.image.primary > img'),
          $bg,
          options,
          $hiddenhack = $this.find("#hiddenhack");
          console.log('hidden', $hiddenhack);

        // No primary image? Bail.
          if ($primaryImg.length == 0)
            return;

        // Hack: IE8 fallback.
          if (skel.vars.IEVersion < 9) {

            $this
              .css('background-image', 'url("' + $primaryImg.attr('src') + '")')
              .css('-ms-behavior', 'url("css/ie/backgroundsize.min.htc")');

            return;

          }

        // Create bg and append it to body.
          $bg = $('<div class="main-bg" id="' + $this.attr('id') + '-bg"></div>')
            .css('background-image', ('url("' + $hiddenhack.attr('src') + '"),' + ' url("' + $primaryImg.attr('src') + '")'))
            .appendTo($body);

        // Scrollex.
          options = {
            mode: 'middle',
            delay: 200,
            top: '-10vh',
            bottom: '-10vh'
          };

          if (skel.canUse('transition')) {

            options.init = function() { $bg.removeClass('active'); };
            options.enter = function() { $bg.addClass('active'); };
            options.leave = function() { $bg.removeClass('active'); };

          }
          else {

            $bg
              .css('opacity', 1)
              .hide();

            options.init = function() { $bg.fadeOut(0); };
            options.enter = function() { $bg.fadeIn(400); };
            options.leave = function() { $bg.fadeOut(400); };

          }

          $this.scrollex(options);

      });

  });

})(jQuery);
